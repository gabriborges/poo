num=int(input("Quantidade de numeros: "))
maior=float(input("Digite o numero 1: "))
contador=1

for i in range(num-1):
  aux=float(input("Digite o numero "+ str(i+2) + ": "))
  if aux>maior:
    maior=aux
  elif aux==maior:
    contador=contador+1
  else:
    pass
print("Quantidade de vezes que o numero "+str(maior)+" se repete: "+str(contador))