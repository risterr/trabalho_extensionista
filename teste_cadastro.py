"""Teste funcional: simula o preenchimento do formulario e confere se salvou."""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'controle_devolucao.settings')
django.setup()

from django.test import Client
from devolucoes.models import Devolucao

cliente = Client()

antes = Devolucao.objects.count()
print('Registros antes do teste:', antes)

resposta = cliente.post('/', {
    'codigo_produto': 'Kit10InfantilRosa',
    'nome_produto': 'Kit 10 Cabides Infantis de Veludo Rosa',
    'marketplace': 'Shopee',
    'motivo': 'Produto avariado',
    'situacao': 'Aguardando avaliação',
    'valor': '289.90',
    'data_devolucao': '2026-09-16',
    'observacao': 'Registro criado durante o teste funcional do sistema.',
})

print('Status do POST:', resposta.status_code, '(302 = salvou e redirecionou)')
print('Registros depois do teste:', Devolucao.objects.count())
print('Ultimo registro salvo:', Devolucao.objects.last())

# teste de validacao: enviar formulario vazio nao deve salvar nada
resposta_vazia = cliente.post('/', {})
print('\nTeste de validacao (formulario vazio):')
print('Status:', resposta_vazia.status_code, '(200 = voltou com erros, nao salvou)')
print('Registros no banco:', Devolucao.objects.count())

# confere se as outras telas carregam
for url in ['/lista/', '/dashboard/', '/lista/?marketplace=Shopee']:
    print(url, '->', cliente.get(url).status_code)
