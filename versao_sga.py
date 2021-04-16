import psycopg2
import os
from pymongo import MongoClient
import sys
from time import gmtime, strftime

# Declaração variáveis globais
pg_user = 'postgres'
pg_senha = '<senha do usuário PostgreSQL>'
pg_databases = os.environ['pg_databases'].split(',')
clientes = []

# tratamento dos parâmetros via linha de comando
parametros = sys.argv
debugar = False

if len(parametros) > 1:
    debugar = parametros[1] == 'true'  # Habilita o modo de teste
# fim do tratamento dos parâmetros


# Função que busca as informações no banco de dados Postgres
def coleta_dados():

    for banco in pg_databases:

        # Cria a conexão com o banco de dados PostgreSQL
        conn = psycopg2.connect(
            host="localhost",
            database=banco,
            user=pg_user,
            password=pg_senha
        )

        # Cria um cursor para obter as informações desejadas no PostgreSQL
        cur = conn.cursor()

        # Executa uma query buscando os dados desejados
        cur.execute(
            "select cfgconteudo from cfg where cfgcampo in ('LICCNPJ', 'LICRAZAO', 'VERSAOSIS') order by cfgcampo")

        # Armazena o resultado da query na variável response
        response = cur.fetchall()

        # Cria um dicionário com as respectivas chaves e valores
        cliente = {"razao": response[1][0], "cnpj": response[0][0], "versao": response[2][0],
                   "data_verificacao": str(strftime('%d/%m/%Y %H:%M'))}

        # Adiciona o dicionario criado acima em uma lista
        clientes.append(cliente)

        # Encerra o cursor
        cur.close()

        # Encerra a conexão com o banco de dados
        conn.close()
    grava_dados()


# Função responsável por gravar no banco MongoDB as informações necessárias.
def grava_dados():

    #  Cria a conexão com o servidor Mongo DB
    conn = MongoClient("<link de acesso ao banco mongoDB>")

    # Instanciado o banco de dado que será utilizado
    if debugar:
        db = conn.test
    else:
        db = conn.clients_retornodb

    # Instanciada a collection que será utilizada dentro do banco clients_retornodb
    if debugar:
        collection = db.teste
    else:
        collection = db.clients

    # Laço de repetição para inclusão das informações no banco
    for cliente in clientes:

        # Utilizado um upsert onde, caso exista a informação no banco, a mesma será atualizada, senão, será inserida
        collection.find_one_and_update({'cnpj': cliente['cnpj']}, {
                                       '$set': cliente}, upsert=True)

    # Limpa as informações da variável global clientes
    clientes.clear()

    # Encerra a conexão com o banco de dados MongoDB
    conn.close()


if __name__ == "__main__":
    coleta_dados()
