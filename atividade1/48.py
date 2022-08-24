import os
os.system('cls')

segundos=int(input("Altura do degrau da escada: "))

horas = segundos//3600
minutos = (segundos%3600)//60
segundos = (segundos%3600)%60

print(str(horas)+":"+str(minutos)+":"+str(segundos))
