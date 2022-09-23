contas = []
contas_dic = {}

op_contas = 0


def nova_conta():
    numero = op_contas
    titular = str(input("Nome do titular: "))
    saldo = 0
    conta = {"Numero": numero, "Titular": titular, "Saldo": saldo}
    contas.append(conta)
    print(contas)
    op_contas += 1


def menu1():
    op_menu = int(
        input(" 1- Cadastrar Nova Conta \n 2- Encontrar uma conta\n"))
    if op_menu == 1:
        nova_conta()


menu1()

print(contas[0]["Numero"])
