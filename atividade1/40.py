import os
os.system('cls')

diaria=30.00

dias=int(input("Quantidade de dias: "))

bruto=diaria*dias
liquido=(bruto/100)*92

print("Valor liquido: R$"+str("{:.2f}".format(liquido)))