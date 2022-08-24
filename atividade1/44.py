import os
os.system('cls')

altura=float(input("Altura do degrau da escada: "))
objetivo=float(input("Altura a ser alcançada: "))

degraus = objetivo/altura

print("Quantidade de degraus necessaria: " + str(degraus))
