# select a distribution from numpy
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution

#Distribución de Pareto
from math import dist
from matplotlib import pyplot
import numpy
import matplotlib

data = numpy.random.pareto(1234,3333)
print(data)
pyplot.hist(data)
pyplot.show()