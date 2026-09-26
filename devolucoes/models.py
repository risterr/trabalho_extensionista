from django.db import models

# funcionarios que podem usar o sistema (id, nome)
# pra adicionar alguem novo na equipe, e so incluir aqui
FUNCIONARIOS_CADASTRADOS = [
    ('01', 'Walter'),
    ('02', 'Pedro'),
    ('03', 'Enzo'),
    ('04', 'Raphael'),
]

class Devolucao(models.Model):
    # produtos que a empresa cadastra nos marketplaces (codigo, nome, valor)
    # esses sao os produtos que aparecem pra escolher no formulario
    PRODUTOS_CADASTRADOS = [
    ('Kit10InfantilRosa', 'Kit 10 Cabides Infantis de Veludo Rosa', 25.90),
    ('Plastificadora110v', 'Plastificadora Poliseladora 110v', 319.90),
    ('Jogo4PanelasBege', 'Jogo de 4 Panelas Beges Para Fogão de Indução', 419.90),
    ('Bike120kg', 'Bicicleta Ergométrica Pequena Portátil Até 120kg', 619.90),
    ('Lixeira40L', 'Lixeira de Alumínio 40L Com Pedal', 98.90),
    ('InfladorAzul220vMedidor', 'Inflador de Balão Azul 220v com Medidor de MDF', 149.90),
    ('CercadinhoAmarelo', 'Cercadinho Amarelo para Bebês', 179.90),
    ('Paint110v', 'Paint Pistola de Pintura 110v com Alça', 149.90),
    ('VaralPortátil', 'Varal Portátil com 3 Andares Para Apartamento', 99.90),
    ('Kit50CabidePreto', 'Kit 50 Cabides Tamanho 45cm de Veludo Preto', 89.90),
    ('EscorredorPequeno', 'Escorredor de Louças Pequeno 50cm 2 Andares', 69.90),
    ('VasoCD19', 'Vaso de Polietileno Vermelho 65cm Sem Prato', 179.90),
    ('LixeiraFralda', 'Lixeira Para Fralda Infantil Rosa', 89.90),
    ]

    # monta as opcoes do select juntando codigo e nome, tipo "PRD-1001 - Furadeira..."
    CODIGO_PRODUTO_CHOICES = [
        (codigo, codigo + ' - ' + nome) for codigo, nome, valor in PRODUTOS_CADASTRADOS
    ]

    # opcoes de marketplace onde a venda foi feita
    MARKETPLACES = [
        ('Mercado Livre', 'Mercado Livre'),
        ('Shopee', 'Shopee'),
        ('Magazine Luiza', 'Magazine Luiza'),
        ('Casas Bahia', 'Casas Bahia'),
        ('Shein', 'Shein'),
        ('Leroy Merlin', 'Leroy Merlin'),
        ('Madeira Madeira', 'Madeira Madeira'),
        ('Tiktok Shop', 'Tiktok Shop'),
        ('Outro', 'Outro'),
    ]

    # motivos de devolucao mais comuns na empresa
    MOTIVOS = [
        ('Produto avariado', 'Produto avariado'),
        ('Produto errado', 'Produto errado'),
        ('Desistencia do cliente', 'Desistência do cliente'),
        ('Peca faltando', 'Peça faltando'),
        ('Atraso na entrega', 'Atraso na entrega'),
        ('Outro', 'Outro'),
    ]

    # situacao da mercadoria depois que ela chega de volta no estoque
    SITUACOES = [
        ('Aguardando avaliação', 'Aguardando avaliação'),
        ('Revenda', 'Revenda'),
        ('Descarte', 'Descarte'),
    ]

    codigo_produto = models.CharField('Produto', max_length=30, choices=CODIGO_PRODUTO_CHOICES)
    nome_produto = models.CharField('Nome do produto', max_length=120, blank=True)
    marketplace = models.CharField('Marketplace', max_length=40, choices=MARKETPLACES)
    motivo = models.CharField('Motivo da devolucao', max_length=40, choices=MOTIVOS)
    situacao = models.CharField('Situacao', max_length=40, choices=SITUACOES, default='Aguardando avaliacao')
    valor = models.DecimalField('Valor do produto (R$)', max_digits=10, decimal_places=2)
    data_devolucao = models.DateField('Data da devolucao')
    observacao = models.TextField('Observacao', blank=True)
    registrado_por = models.CharField('Registrado por', max_length=60, blank=True)
    registrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codigo_produto + ' - ' + self.nome_produto
