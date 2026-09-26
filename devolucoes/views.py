from functools import wraps
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Count, Sum
from .models import Devolucao, FUNCIONARIOS_CADASTRADOS
from .forms import DevolucaoForm


def exige_identificacao(view_func):
    """So deixa passar se o funcionario ja escolheu o ID na tela inicial.
    Se nao escolheu ainda, manda pra tela de identificacao."""
    @wraps(view_func)
    def view_protegida(request, *args, **kwargs):
        if not request.session.get('funcionario_nome'):
            return redirect(reverse('identificar') + '?next=' + request.path)
        return view_func(request, *args, **kwargs)
    return view_protegida


def identificar(request):
    """Tela inicial: o funcionario escolhe o ID dele antes de usar o sistema."""
    proxima_pagina = request.GET.get('next', 'registrar')

    if request.method == 'POST':
        id_escolhido = request.POST.get('funcionario_id')
        funcionarios = dict(FUNCIONARIOS_CADASTRADOS)
        if id_escolhido in funcionarios:
            request.session['funcionario_id'] = id_escolhido
            request.session['funcionario_nome'] = funcionarios[id_escolhido]
            return redirect(proxima_pagina)
        erro = 'Selecione um funcionario valido da lista.'
        return render(request, 'devolucoes/identificar.html', {
            'funcionarios': FUNCIONARIOS_CADASTRADOS, 'erro': erro,
        })

    return render(request, 'devolucoes/identificar.html', {
        'funcionarios': FUNCIONARIOS_CADASTRADOS,
    })


def sair(request):
    """Limpa a identificacao, pra outro funcionario usar o sistema."""
    request.session.flush()
    return redirect('identificar')


@exige_identificacao
def registrar(request):
    """Tela que o pessoal do setor logistico usa pra registrar a devolucao."""
    if request.method == 'POST':
        form = DevolucaoForm(request.POST)
        if form.is_valid():
            devolucao = form.save(commit=False)
            # busca nome e valor do produto a partir do codigo escolhido no select
            # PRODUTOS_CADASTRADOS tem (codigo, nome, valor), entao monta um dict codigo -> (nome, valor)
            produtos = {codigo: (nome, valor) for codigo, nome, valor in Devolucao.PRODUTOS_CADASTRADOS}
            nome, valor = produtos.get(devolucao.codigo_produto, ('', 0))
            devolucao.nome_produto = nome
            devolucao.valor = valor
            devolucao.registrado_por = request.session.get('funcionario_nome', '')
            devolucao.save()
            return redirect('lista')
    else:
        form = DevolucaoForm()

    return render(request, 'devolucoes/registrar.html', {'form': form})


@exige_identificacao
def lista(request):
    """Lista todas as devolucoes registradas, com filtro simples."""
    devolucoes = Devolucao.objects.all().order_by('-data_devolucao')

    # filtro por marketplace (vem da URL, tipo ?marketplace=Shopee)
    marketplace = request.GET.get('marketplace')
    if marketplace:
        devolucoes = devolucoes.filter(marketplace=marketplace)

    contexto = {
        'devolucoes': devolucoes,
        'marketplaces': Devolucao.MARKETPLACES,
        'marketplace_escolhido': marketplace,
    }
    return render(request, 'devolucoes/lista.html', contexto)


@exige_identificacao
def excluir(request, id):
    """Apaga uma devolucao da lista. So exclui se vier via POST (com confirmacao no template)."""
    devolucao = get_object_or_404(Devolucao, id=id)
    if request.method == 'POST':
        devolucao.delete()
        return redirect('lista')
    return redirect('lista')


@exige_identificacao
def dashboard(request):
    """Painel com os numeros que a gestao pediu."""
    total = Devolucao.objects.count()
    valor_total = Devolucao.objects.aggregate(soma=Sum('valor'))['soma'] or 0

    # produtos que mais voltaram
    por_produto = (Devolucao.objects
                   .values('nome_produto')
                   .annotate(qtd=Count('id'))
                   .order_by('-qtd')[:5])

    # quanto de prejuizo por marketplace
    por_marketplace = (Devolucao.objects
                       .values('marketplace')
                       .annotate(qtd=Count('id'), valor=Sum('valor'))
                       .order_by('-valor'))

    # motivos mais frequentes
    por_motivo = (Devolucao.objects
                  .values('motivo')
                  .annotate(qtd=Count('id'))
                  .order_by('-qtd'))

    # calcula a porcentagem de cada motivo pra desenhar as barras
    lista_motivos = []
    for item in por_motivo:
        if total > 0:
            porcentagem = round(item['qtd'] * 100 / total)
        else:
            porcentagem = 0
        lista_motivos.append({
            'motivo': item['motivo'],
            'qtd': item['qtd'],
            'porcentagem': porcentagem,
        })

    descarte = Devolucao.objects.filter(situacao='Descarte').count()

    # quantas devolucoes cada funcionario registrou
    por_funcionario = (Devolucao.objects
                       .values('registrado_por')
                       .annotate(qtd=Count('id'))
                       .order_by('-qtd'))

    contexto = {
        'total': total,
        'valor_total': valor_total,
        'por_produto': por_produto,
        'por_marketplace': por_marketplace,
        'por_motivo': lista_motivos,
        'descarte': descarte,
        'por_funcionario': por_funcionario,
    }
    return render(request, 'devolucoes/dashboard.html', contexto)
