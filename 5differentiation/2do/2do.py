#
# please refer to PPT file
# for exercise
#

import numpy as np

def derivative(f,a,method='central',h=0.01):
    if method == 'central':
        return (f(a + h) - f(a - h))/(2*h)
    elif method == 'forward':
        return (f(a + h) - f(a))/h
    elif method == 'backward':
        return (f(a) - f(a - h))/h
    else:
        raise ValueError("Method must be 'central', 'forward' or 'backward'.")
def f(x):
    return (np.sin(2*x)**3)/((x**4)+1)

print("Diferenciacion finita regresiva: " + str(derivative(f,2.54,method='backward',h=1e-15)))
print("Diferenciacion finita centrada: " + str(derivative(f,2.54,method='central',h=1e-15)))
print("Diferenciacion finita progresiva: " + str(derivative(f,2.54,method='forward',h=1e-15)))