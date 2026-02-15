import pymysql
import os
from dotenv import load_dotenv

load_dotenv() #carrega o arquivo .env se existir

def conectar_banco():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

def verificacao_banco(conta_id):
    conexao = conectar_banco() #Abertura de conexão com o banco de dados MYSQL
    cursor = conexao.cursor()
    cursor.execute(
        'SELECT 1 FROM contas WHERE conta_id = %s',
        (conta_id,)
    ) #Executar os comando SQL no banco de dados
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado is not None #Transforma o resultado em True or False

def salvar_conta_banco(nova_conta):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(
        'INSERT INTO contas (conta_id,descricao) VALUES (%s,%s)',
        (nova_conta['conta_id'],nova_conta['descricao'])
    )
    conexao.commit() #Salva as alterações/inserções no banco de dados
    cursor.close()
    conexao.close()

def salvar_registro_banco(novo_registro):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(
        'INSERT INTO lancamentos (data_registro,contaDebito_id,contaCredito_id,valor,historico) VALUES (%s,%s,%s,%s,%s)',
        (novo_registro['data_registro'],novo_registro['contaDebito_id'],novo_registro['contaCredito_id'],
         novo_registro['valor'],novo_registro['historico'])
    )
    conexao.commit()
    cursor.close()
    conexao.close()

def exibir_lancamentos():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(
        'SELECT * FROM lancamentos'
    )
    resultados = cursor.fetchall()
    # conexao.commit() -- Não é necessário para SELECT; usado paenas para confirmar/salvar alterações
    cursor.close()
    conexao.close()
    return resultados