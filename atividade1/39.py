import os
os.system('cls')

premio=780000.00
premio_porcentagem=780000.00/100

primeiro=premio_porcentagem*46
premio=premio-primeiro

segundo=premio_porcentagem*32
premio=premio-segundo

terceiro=premio

print("Premio do primeiro ganhador: "+str(primeiro))
print("Premio do segundo ganhador: "+str(segundo))
print("Premio do terceiro ganhador: "+str(terceiro))
print(primeiro+segundo+terceiro)