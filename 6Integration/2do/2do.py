#
# please refer to PPT file
# for exercise
#
#parte 1
from math import cos, exp, pi, sin, sqrt
from scipy.integrate import quad

# function we want to integrate
def f(x):
    return 2*sin(sqrt(x))-x

# call quad to integrate f from -2 to 2
res, err = quad(f, 0, 1.9724)

print("El resultado de la integración del ejercicio 1 es: {:f} (Variación de: +-{:g})"
    .format(res, err))

#parte 2
from math import cos, exp, pi
from scipy.integrate import quad

# function we want to integrate
def f(x):
    return (7**(-x))+3

# call quad to integrate f from -2 to 2
res, err = quad(f, -1, 2)

print("El resultado de la integración del ejercicio 2 es: {:f} (Variación de: +-{:g})"
    .format(res, err))