#
# select a distribution from random
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#
import random
import matplotlib.pyplot as plt

nums = []
low = 10
mode = 20
high = 30

  
for i in range(10000):
    valor = random.triangular(low, high, mode)
    nums.append(valor)

print(nums)
plt.hist(nums, bins = 200)
plt.show()