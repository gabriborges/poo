import math


def calcular_volume(altura, raio):
    volume = math.pi * raio**2 * altura
    print("O volume é: " + str(volume))


calcular_volume(10, 3)
