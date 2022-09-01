anterior = 0
proximo = 0
num=int(input("Digite o numero: "))

while(proximo < num):
  print(proximo)
  proximo = proximo + anterior
  anterior = proximo - anterior
  if(proximo == 0):
    proximo = proximo + 1

if proximo>=num:
  print(proximo)
  proximo = proximo + anterior
  anterior = proximo - anterior