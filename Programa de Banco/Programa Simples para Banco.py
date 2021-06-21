
cadastros = []

# Definições
def cadastro():  #Cadastro
    print('============= Cadastro =============')
    nome = str(input('Nome: '))
    cpf = str(input('CPF: '))
    banco = str(input('Banco: '))
    agencia = int(input('Agencia: '))
    numero = int(input('Numero: '))
    conta = int(input('Conta: '))
    valor = 5000
    pessoa = [nome, cpf, banco, agencia, numero, conta, valor]
    cadastros.append(pessoa)
    print('Cadastro efetuado.')

def deposita_sacar_transferir(): #Funções (Sacar, Transferir, Depositar)
    # Login da conta.
    print('============= Login =============')
    banco = str(input('Banco: '))
    agencia = int(input('Agencia: '))
    numero = int(input('Numero: '))
    conta = int(input('Conta: '))

    for a in range(0, len(cadastros)):
        if cadastros[a][2] == banco and cadastros[a][3] == agencia and cadastros[a][4] == numero and cadastros[a][5] == conta:
            #Pagina inicial de acesso.
            print('============= Menu =============')
            print(f'Titular: {cadastros[a][0]}')
            print(f'Saldo: R${cadastros[a][-1]}')
            print('Depositar $                digite 1')
            print('Sacar $                    digite 2')
            print('Transferir $               digite 3')
            opcao = str(input('Opção: '))
            if opcao == '1':  #Opção de Depositar.
                deposito = float(input('Valor do deposito: R$'))
                cadastros[a][-1] = int(cadastros[a][-1]) + deposito 
                print(f'Saldo: R${cadastros[a][-1]}')
            elif opcao == '2': #Opção de Sacar.
                saque = float(input('Valor do saque: R$'))
                saldo = int(cadastros[a][-1]) - saque
                if saldo < 0:
                    print(f'Saldo indisponivel. Saldo: R${cadastros[a][-1]}')
                else: #Opção de Transferencia.
                    cadastros[a][-1] = int(cadastros[a][-1]) - saque
                    print(f'Novo Saldo: R${cadastros[a][-1]}')
            else:
                transferencia = float(input('Valor da transferencia: R$'))
                pessoa = input('CPF da pessoa: ')
                #Transeferencia de dinheiro para outro usuario cadastrado.
                for b in range(0, len(cadastros)):
                    if cadastros[b][1] == pessoa:
                        cadastros[b][-1] = cadastros[b][-1]+transferencia

                saldo = int(cadastros[a][-1]) - transferencia
                print(f'Saldo: R${cadastros[a][-1]}')
                if saldo < 0:
                    print(f'Saldo indisponivel. Saldo: R${cadastros[a][-1]}')
                else:
                    cadastros[a][-1] = int(cadastros[a][-1]) - transferencia
                    print(f'Novo Saldo: R${cadastros[a][-1]}')

# Programa
import os
while True:
    print('============= Banco =============')
    print('Novo Cadastro            digite 1')
    print('Entrar na Conta          digite 2')
    opcao = input('Opção: ')

    if opcao == '1':
        os.system('cls')
        cadastro()
        
    elif opcao == '2':
        os.system('cls')
        deposita_sacar_transferir()



