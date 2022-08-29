aux=int(input("Digite o numero 1:"))
maior=menor=aux
for i in range(4):
  aux=int(input("Digite o numero "+str(i+2)+":"))
  if aux>=maior:
    maior=aux
  if aux<=menor:
    menor=aux
    
print("Maior: "+str(maior))
print("Menor: "+str(menor))