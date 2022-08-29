n=j=0
for i in range(10):
  aux=int(input("Digite o inteiro "+str(i+1)+":"))
  n=aux+n
  j=j+1
print("Media: "+str(n/j))