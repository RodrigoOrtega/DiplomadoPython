#
# generate a function to produce points 
# to be used as x-axis
# 
# INPUT
# -> a initial point
# -> b final point
# -> c increment
#
# OUTPUT
# <- list of points
#
# for instance for this range [1,10,.1]
# it will produce 100 points
# [1.0, 1.1, ... , 9.9, 10]
#
import matplotlib.pyplot as plt
import numpy as np

# -> a initial point
a = 0
# -> b final point
b = 3
# -> c increment
c = 0.1

fig = plt.subplots(figsize=(12, 6))

x = np.array([0, 1, 2, 3])
plt.plot(y, color='black')

plt.xticks(np.arange(a, b+0.1, c))
plt.yticks(np.arange(a, b+0.1, c))

plt.show()