import os
os.system('cls')

valor=float(input("Valor: "))

desconto = valor*0.9
parcelamento = valor/3
a_vista = desconto*0.05
parcelada = valor*0.05

print("Total a pagar com desconto: R$" + str("{:.2f}".format(desconto)))
print("Valor de cada parcela: R$" + str("{:.2f}".format(parcelamento)))
print("Comissão do pagamento a vista: R$" + str("{:.2f}".format(a_vista)))
print("Comissão do pagamento parcelado: R$" + str("{:.2f}".format(parcelada)))