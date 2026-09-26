"""Script simples para inserir dados de teste no sistema.
ATENÇÃO: os dados dos produtos abaixo são reais da loja RRister Imports, alguns produtos saíram de estoque, mas foram adicionados apenas para testar as telas e o dashboard.
"""
import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'controle_devolucao.settings')
django.setup()

from devolucoes.models import Devolucao

dados = [
    ('Kit10InfantilRosa', 'Kit 10 Cabides Infantis de Veludo Rosa', 'Mercado Livre', 'Produto avariado', 'Descarte', 289.90, date(2026, 8, 3)),
    ('Plastificadora110v', 'Plastificadora Poliseladora 110v', 'Shopee', 'Produto avariado', 'Descarte', 289.90, date(2026, 8, 11)),
    ('Jogo4PanelasBege', 'Jogo de 4 Panelas Beges Para Fogão de Indução', 'Magazine Luiza', 'Peca faltando', 'Revenda', 289.90, date(2026, 8, 19)),
    ('Bike120kg', 'Bicicleta Ergométrica Pequena Portátil Até 120kg', 'Shopee', 'Desistencia do cliente', 'Revenda', 89.00, date(2026, 8, 5)),
    ('Lixeira40L', 'Lixeira de Alumínio 40L Com Pedal', 'Mercado Livre', 'Produto errado', 'Revenda', 89.00, date(2026, 8, 14)),
    ('InfladorAzul220vMedidor', 'Inflador de Balão Azul 220v com Medidor de MDF', 'Casas Bahia', 'Produto avariado', 'Descarte', 129.50, date(2026, 8, 7)),
    ('TorneiraMZ19', 'Torneira Gourmet MZ19 Quente-Frio', 'Leroy Merlin', 'Atraso na entrega', 'Revenda', 129.50, date(2026, 8, 21)),
    ('CercadinhoAmarelo', 'Cercadinho Amarelo para Bebês', 'Madeira Madeira', 'Produto avariado', 'Descarte', 549.00, date(2026, 8, 9)),
    ('Paint110v', 'Paint Pistola de Pintura 110v com Alça', 'Magazine Luiza', 'Peca faltando', 'Aguardando avaliacao', 549.00, date(2026, 8, 25)),
    ('VaralPortátil', 'Varal Portátil com 3 Andares Para Apartamento', 'Shein', 'Desistencia do cliente', 'Revenda', 45.90, date(2026, 8, 12)),
    ('Kit50CabidePreto', 'Kit 50 Cabides Tamanho 45cm de Veludo Preto', 'TikTok Shop', 'Produto avariado', 'Descarte', 159.00, date(2026, 8, 15)),
    ('EscorredorPequeno', 'Escorredor de Louças Pequeno 50cm 2 Andares', 'Mercado Livre', 'Produto avariado', 'Aguardando avaliacao', 219.00, date(2026, 8, 18)),
    ('VasoCD19', 'Vaso de Polietileno Vermelho 65cm Sem Prato', 'Casas Bahia', 'Desistencia do cliente', 'Revenda', 219.00, date(2026, 8, 29)),
    ('LixeiraFralda', 'Lixeira Para Fralda Infantil Rosa', 'Shein', 'Produto errado', 'Revenda', 39.90, date(2026, 8, 22)),
]

Devolucao.objects.all().delete()

for codigo, nome, marketplace, motivo, situacao, valor, data in dados:
    Devolucao.objects.create(
        codigo_produto=codigo,
        nome_produto=nome,
        marketplace=marketplace,
        motivo=motivo,
        situacao=situacao,
        valor=valor,
        data_devolucao=data,
        observacao='Registro de teste.',
    )

print('Foram inseridos', Devolucao.objects.count(), 'registros de teste.')
