#
# first homework of the day
#
import random

direcciones = ("norte","este","sur","oeste")

def brujula(veces):
    i = 0
    while i < veces:
        print("Dirección no." + str(i+1) + ": " +str(random.choice(direcciones)))
        i+=1

print("Generador lados de brújula")
print("Escriba la cantidad de veces que desea utilizar la brújula:")
veces = int(input())
brujula(veces)