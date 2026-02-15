from database import verificacao_banco,salvar_conta_banco,salvar_registro_banco
from datetime import datetime
from decimal import Decimal

def inserir_registros():
    novo_registro = {}
    data_registro = 0
    while True:
        data = input('Data do registro (DD/MM/AAAA): ')
        try:
            data_registro = datetime.strptime(data, '%d/%m/%Y').date()
            break
        except ValueError:
            print('Data inválida! Use o formato DD-MM-AAAA.')
            continue
    novo_registro['data_registro'] = data_registro
    while True:
        contad = int(input('Código Conta Débito: '))
        conta_id = contad
        novo_registro['contaDebito_id'] = obter_criar_conta(conta_id)
        contac = int(input('Código Conta Crédito: '))
        conta_id = contac
        novo_registro['contaCredito_id'] = obter_criar_conta(conta_id)
        if contad == contac:
            print('Não é viável as contas Débito e Crédito serem iguais. Tente novamente...')
            continue
        else:
            break
    while True:
        valor = input('Valor: R$ ')
        valor = Decimal(valor)
        if valor <= 0:
            print('O valor não pode ser menor o igual a ZERO. Tente novamente...')
            continue
        else:
            break
    novo_registro['valor'] = valor
    novo_registro['historico'] = str(input('Descrição: '))
    salvar_registro_banco(novo_registro)
    return novo_registro

def cadastro_contas():
    conta = {'conta_id':int(input('Informe o código numérico da conta: ')),
             'descricao': str(input('Informe o nome dessa conta: '))}
    return conta

def obter_criar_conta(conta_id):
    conta_existe = verificacao_banco(conta_id) #Consulta no banco de dados -SELECT- e retorna True or False
    if not conta_existe:
        print('Essa conta não existe em nossa base. Vamos cadastrá-la!')
        nova_conta = cadastro_contas()
        salvar_conta_banco(nova_conta) #Cadastrar nova conta no banco de dados - INSERT-
        return nova_conta['conta_id']
    return conta_id