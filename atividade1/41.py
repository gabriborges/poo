import os
os.system('cls')

valor=float(input("Valor da hora: "))

horas=int(input("Quantidade de horas: "))

pagamento=(valor*horas)*1.1

print("Valor a ser pago: R$" + str("{:.2f}".format(pagamento)))