from funcoes import inserir_registros,cadastro_contas
from database import exibir_lancamentos

print('--*--'*7)
print('      BEM-VINDO(A) AO SISCONT')
print('--*--'*7)

opcao = 0
lancamentos = []
contas = []

while True:
    print('-'*16,'*','-'*16)
    print('      MENU DE FUNCIONALIDADES')
    print('-'*35)
    print('1. Lançamentos Contábeis')
    print('2. Contas')
    print('3. Sair do SISCONT')
    print('-'*35)
    opcao = int(input('Digite o número referente a funcionalidade desejada: '))

    if opcao <= 0 or opcao > 3:
        print('Opção inválida! Tente novamente.')
        continue
    elif opcao == 1:
        while True:
            print('-' * 16, '*', '-' * 16)
            print('      LANÇAMENTOS CONTÁBEIS')
            print('-' * 35)
            print('1. Inserir um novo registro')
            print('2. Visualizar registros existentes')
            print('3. Voltar ao Menu de Funcionalidades')
            print('-' * 35)
            opcao_lancamento = int(input('Digite o número referente a ação desejada: '))

            if opcao_lancamento == 1:
                while True:
                    lancamentos = inserir_registros()
                    print('Lançamento inserido com sucesso!')
                    repetir_lancamento = str(input('Deseja realizar mais lançamentos (Sim ou Não): ')).upper()
                    if repetir_lancamento == 'SIM':
                        continue
                    elif repetir_lancamento == 'NÃO' or repetir_lancamento == 'NAO':
                        print('Retornando ao menu de Lançamentos Contábeis')
                        break
                continue

            elif opcao_lancamento == 2:
                registros = exibir_lancamentos()
                for i in range(0,len(registros),1):
                    cont = i+1
                    print(f'Registro nº{cont}')
                    print(f'ID: {registros[i][0]}')
                    data = registros[i][1]
                    data_formatada = data.strftime("%d/%m/%Y")
                    print(f'Data: {data_formatada}')
                    print(f'Conta Débito: {registros[i][2]}')
                    print(f'Conta Crédito: {registros[i][3]}')
                    print(f'Valor: R$ {registros[i][4]}')
                    print(f'Descrição: {registros[i][5]}\n')
                continue

            elif opcao_lancamento == 3:
                print('Retornando ao menu de Funcionalidades')
            break
        continue

    elif opcao == 2:
        while True:
            print('-' * 16, '*', '-' * 16)
            print('               CONTAS')
            print('-' * 35)
            print('1. Cadastrar uma nova conta')
            print('2. Visualizar contas existentes')
            print('3. Voltar ao Menu de Funcionalidades')
            print('-' * 35)
            opcao_contas = int(input('Digite o número referente a ação desejada: '))

            if opcao_contas == 1:
                while True:
                    cadastro_contas()
                    contas = cadastro_contas()
                    print('Conta cadastrada com sucesso!')
                    repetir_cadastro_conta = str(input('Deseja cadastrar mais contas (Sim ou Não): ')).upper
                    if repetir_cadastro_conta == 'SIM':
                        continue
                    elif repetir_cadastro_conta == 'NÃO' or repetir_cadastro_conta == 'NAO':
                        print('Retornando ao Menu Contas...')
                        break
                continue
            elif opcao == 2:
                print(contas)
                continue
            elif opcao == 3:
                break
        continue

    elif opcao == 3:
        print('Obrigado por utilizar nossos serviços!')
        print('Encerrando programa...')
    break
