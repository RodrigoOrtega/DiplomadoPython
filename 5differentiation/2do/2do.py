#
# please refer to PPT file
# for exercise
#

import numpy as np
from scipy.misc import derivative

def f(x):

    return (np.sin(2*x)**3)/((x**4)+1) 

print(derivative(f, 2.45, dx=1e-6))