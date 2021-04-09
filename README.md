# Projeto SGAVersion
Aplicativo criado para fim de sanar uma necessidade que tinhamos na empresa para fazer um controle de versão do software SGAPetro nos clientes.

--- 
Para executar como teste e salvar as informações no banco de dados de testes, é necessário executar o arquivo .py pela linha de comando com a palavra 'true', minusculo mesmo, na frente do nome.

Exemplo: 

    test_sga_version.py true

## Atenção!
Caso ocorra algum erro ao conectar com o MongoDB, é necessário executar os seguintes comandos no terminal como Administrador.

    python -m pip install psycopg2[srv]
    python -m pip install psycopg2[tls]
