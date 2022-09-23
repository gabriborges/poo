import os
os.system('cls')

contas = []
contas_dic = {}

op_contas=1

def mostrar_conta():
    for i in range(len(contas)):
        print("\nInformações da conta: \n")
        print("\nNumero: "+str(contas[i]["Numero"])+"\nTitular: "+str(contas[i]["Titular"])+"\nSaldo: R$"+str(contas[i]["Saldo"])+"\n")

def nova_conta():
    global op_contas
    print("----Crie uma nova conta----")
    numero = op_contas
    titular = str(input("Nome do titular: "))
    saldo = 0.0
    conta = {"Numero": numero, "Titular": titular, "Saldo": saldo}
    contas.append(conta)
    mostrar_conta()
    op_contas+=1

def remover_conta():
    for i in range(len(contas)):
        print(contas[i])

def realizar_tranferencia():
    valor=float(input("Valor a ser tranferido: "))
    conta_dest=int(input("Conta destinaria da transferencia: "))
    for i in range(len(contas)):
        if contas[i]["Numero"]==conta_alvo:
            if contas[i]["Saldo"]>=valor:
                for j in range(len(contas)):
                    if contas[j]["Numero"]==conta_dest:
                        contas[j]["Saldo"]+=valor
                        print("R$"+str(valor)+" acabam de ser tranferisos para a conta "+str(conta_dest))

def exibir_saldo():
    for i in range(len(contas)):
        if contas[i]["Numero"]==conta_alvo:
            print("Seu saldo é R$"+contas[i]["Saldo"])

def depositar():
    for i in range(len(contas)):
        if contas[i]["Numero"]==conta_alvo:
            deposito=float(input("Valor a ser depositado: "))
            contas[i]["Saldo"]+=deposito

def encontrar_conta():
    global conta_alvo
    conta_alvo=int(input("\nDigite o número da conta: "))
    for i in range(len(contas)):
        if contas[i]["Numero"]==conta_alvo:
            op_encontrar = int(input("\n  1- Remover Conta \n 2- Realizar transferência\n 3- Exibir saldo\n  4- Deposita Valor 5- Voltar para o menu inicial\n "))
            if op_encontrar == 1:
                remover_conta()
            elif op_encontrar==2:
                realizar_tranferencia()
            elif op_encontrar==3:
                exibir_saldo()
            elif op_encontrar==4:
                depositar()
            elif op_encontrar==5:
                menu_principal()
            else:
                print("\nOpção inválida, tente outra.")
                encontrar_conta
    
def remover_conta():
    for i in range(len(contas)):
        if contas[i]["Numero"]==conta_alvo:
            del(contas[i])

def menu_principal():
    op_menu_principal = int(input("\n 1- Cadastrar Nova Conta \n 2- Encontrar uma conta\n"))
    if op_menu_principal == 1:
        nova_conta()
        menu_principal()
    elif op_menu_principal==2:
        encontrar_conta()

menu_principal()