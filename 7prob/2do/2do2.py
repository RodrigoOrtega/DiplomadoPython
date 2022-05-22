# produce 10,000 coin flips
# print how many of them were:
# heads
# tails
import random

moneda = ("aguila", "sol")


def flip(veces):
    conteoAguila = 0
    conteoSol = 0
    i=0
    while i < veces:
        lado = random.choice(moneda)
        if(lado == "aguila"):
            conteoAguila += 1
        if(lado == "sol"):
            conteoSol += 1
        i += 1
    print("La moneda cayó del lado aguila " + str(conteoAguila) + " veces")
    print("La moneda cayó del lado sol " + str(conteoSol) + " veces")


print("¿cuantas veces deseas voltear la moneda?: ")
veces = int(input())
flip(veces)