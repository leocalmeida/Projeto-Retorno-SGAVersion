# Projeto SGAVersion
Esse repositório é apenas do client que roda no computador do cliente, buscando as informações no banco de dados PostgreSQL e gravar as informações obtidas no banco de dados MongoDB.

A aplicação possui 3 partes:

1ª parte é esta, descrita neste repositório, uma aplicação que roda no computador do cliente obtendo as informações necessárias e as grava no banco de dados em núvem. Esse aplicativo foi construído em Python.

2ª parte é uma restAPI, contruída em FLASK, que lê as informações do banco de dados MongoDB e as retorna no formato JSON.
Link para visualizar o funcionamento da restAPI. [Backend da Aplicação](https://sgaversion-backend.herokuapp.com/)
    
3ª parte é o frontend, construida em React, que esctrutura as informações que a restAPI disponibiliza.
Link para visualizar a aplicação em funcionamento. [Frontend da Aplicação](https://sgaversion-frontend.herokuapp.com/)

Aplicativo criado para fim de sanar uma necessidade que tinhamos na empresa para fazer um controle de versão do software SGAPetro nos clientes.

--- 

Para executar como teste o aplicativo que obtem as informações da versão  do SGAPetro que o cliente roda, é necessário executar o arquivo .py pela linha de comando com a palavra 'true', minusculo mesmo, na frente do nome.

Exemplo: 

    test_sga_version.py true

## Atenção!
Caso ocorra algum erro ao conectar com o MongoDB, é necessário executar os seguintes comandos no terminal como Administrador.

    python -m pip install psycopg2[srv]
    python -m pip install psycopg2[tls]
