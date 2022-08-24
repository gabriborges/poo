import os
os.system('cls')

salario=float(input("Salário-base: "))

salario=(salario*1.05)*0.93

print("Salário a receber: R$" + str("{:.2f}".format(salario)))