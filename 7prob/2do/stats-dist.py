#
# OPTIONAL
# requires installing stats
#
# select a distribution from stats
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#

import numpy as np
from scipy.stats import beta
import matplotlib.pyplot

a, b = 2.31, 0.627
values = beta.rvs(a, b, size=4242)
print(values)
matplotlib.pyplot.hist(values)
matplotlib.pyplot.show()