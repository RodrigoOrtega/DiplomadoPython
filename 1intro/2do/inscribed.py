#
# radious of circle inscribed in a tringle
# place here your solution code
#
# zeeAlso
# https://keisan.casio.com/exec/system/1223428152

from math import sqrt


print("Calculadora del radio en centímetros de un círculo inscrito en un triángulo")
print("introduzca longitud del lado a del triángulo")
a = float(input())
print("introduzca longitud del lado b del triángulo")
b = float(input())
print("introduzca longitud del lado c del triángulo")
c = float(input())

if (a + b) < c or (a + c) < b or (b + c) < a:
    print("Las longitudes introducidas no forman un triángulo")
else:
    #Semiperímetro
    s = (a + b + c) / 2

    #Radio del círculo
    r = sqrt((s) * (s - a) * (s - b) * (s - c)) / s
    
    print("la longitud del radio es de " + str(r) + " centímetros")

