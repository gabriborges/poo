import os
os.system('cls')

print("---Horario de inicio---")
horas = int(input("Hora: "))
minutos = int(input("Minuto: "))
Segundos = int(input("Segundo: "))
duracao = int(input("Duração do experimento: "))

segundos = (horas*3600)+(minutos*60)+Segundos+duracao

horas = segundos//3600
minutos = (segundos%3600)//60
segundos = (segundos%3600)%60

print("Horario de termino: "+str(horas)+":"+str(minutos)+":"+str(segundos))
