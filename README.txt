SISTEMA DE CONTROLE DE DEVOLUCAO DE MERCADORIAS
Atividade Extensionista II - UNINTER
Rafaela Rister - RU 5112961

COMO RODAR O PROJETO:

1. Instalar o Django:
   pip install django

2. Criar o banco de dados:
   python manage.py migrate

3. (Opcional) Inserir os dados de teste:
   python popular_teste.py

4. Subir o servidor:
   python manage.py runserver

5. Abrir no navegador:
   http://127.0.0.1:8000/           -> registrar devolucao
   http://127.0.0.1:8000/lista/     -> devolucoes registradas
   http://127.0.0.1:8000/dashboard/ -> dashboard de indicadores

PARA RODAR OS TESTES FUNCIONAIS:
   python teste_cadastro.py

OBSERVACAO: os dados do arquivo popular_teste.py sao ficticios,
criados apenas para testar as telas. Nao sao dados reais da empresa.
