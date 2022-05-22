#
# convert 1st variable as tuple
# convert 2nd variable as dictionary
# convert 3rd variable as list
#
from math import prod
import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')
#vs
#iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data')

print('head',iris.head())
df = pd.DataFrame(iris)
templist = df['sepal length'].values.tolist()
sepalLenght = tuple(templist)
print("Los elementos de sepal lenght en tupla son: ")
print(sepalLenght)
print("el tipo de sepal lenght es: ")
print(type(sepalLenght))

sepalWidth = df['sepal width'].to_dict()
print("Los elementos de sepal width en diccionario son: ")
print(sepalWidth)
print("el tipo de sepal width es: ")
print(type(sepalWidth))

petalLenght = df['petal length'].values.tolist()
print("Los elementos de petal lenght en lista son: ")
print(petalLenght)
print("el tipo de petal lenght es: ")
print(type(petalLenght))