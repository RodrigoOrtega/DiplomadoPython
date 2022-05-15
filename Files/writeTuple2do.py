#
# 2do
#

#t=12,True,3.1,'aCat'
import pickle


print("introduzca la cantidad de registros a almacenar:")
noReg = int(input())
print("Introduzca los valores, presionando enter para introducir el siguiente:")
#creación de la tupla con los valores introducidos
tup = tuple(input() for _ in range(noReg))
#Muestra la tupla antes de crear el archivo
print(tup)

#Creación del archivo
tupleFile = open("tupleFile.pickle", "wb")
pickle.dump(tup, tupleFile)