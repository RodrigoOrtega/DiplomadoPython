#
# please refer to PPT file
# for exercise
#

from numpy import e

def newton(f,Df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Solución encontrada después de:',n,'iteraciones.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Derivada cero, no se encontraron soluciones')
            return None
        xn = xn - fxn/Dfxn
    print('número máximo de iteraciones excedido, no se encontró la solución')
    return None

p = lambda x: e**(2-x)-(7*x)
Dp = lambda x: -e**(2-x)-7
approx = newton(p,Dp,1,1e-10,10)
print(approx)