#
# please refer to PPT file
# for exercise
#

#Ejercicio 1
#Interpolacion lineal
d1 = (-4, -2)
d2 = (1, 5)

def fn(y, d1, d2):
    a = (d2[0] - d1[0]) / (d2[1] - d1[1])
    b = y - d1[1]
    return a * b + d1[0]

print("El resultado de la primer parte de la tarea es: ")
print(fn(3.7, d1, d2))

#Ejercicio 2
#Calculado con el polinomio interpolante de 4 puntos
d1 = (-2,4)
d2 = (-1,-2)
d3 = (3,5)
d4 = (4.3,11)

def fn(x,d1,d2,d3,d4):
    a = (((x-d2[0])*(x-d3[0])*(x-d4[0]))/((d1[0]-d2[0])*(d1[0]-d3[0])*(d1[0]-d4[0])))*d1[1]
    b = (((x-d1[0])*(x-d3[0])*(x-d4[0]))/((d2[0]-d1[0])*(d2[0]-d3[0])*(d2[0]-d4[0])))*d2[1]
    c = (((x-d1[0])*(x-d2[0])*(x-d4[0]))/((d3[0]-d1[0])*(d3[0]-d2[0])*(d3[0]-d4[0])))*d3[1]
    d = (((x-d1[0])*(x-d2[0])*(x-d3[0]))/((d4[0]-d1[0])*(d4[0]-d2[0])*(d4[0]-d3[0])))*d4[1]
    return a+b+c+d

print("El resultado de la segunda parte de la tarea es: ")
print(fn(7.7,d1,d2,d3,d4))

#Ejercicio 3
#Calculado con el polinomio interpolante de Lagrange, librerías de numpy y scipy
import numpy as np
from scipy.interpolate import lagrange

x = np.array([-1, 0, 4, 5])

y = np.array([3, -7, 7, 11])

print("El resultado de la tercer parte de la tarea es: \n" + str(lagrange(x, y)))