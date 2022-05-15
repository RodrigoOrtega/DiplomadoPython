#
# 2do
#

#d={'one':'aaa aaa', 'two':'bbb bbb', 'three':'ccc ccc'}

#Para serializar el archivo
import pickle

print("introduzca la cantidad de registros a almacenar:")
noReg = int(input())
print("Introduzca los campos llave y valor separados por un espacio, ejemplo: lobo negro")
#creación del diccionario con los valores introducidos
dictionary = dict(input().split() for _ in range(noReg))
#Muestra el diccionario antes de crear el archivo
print(dictionary)

#Creación del archivo
dictFile = open("dictFile.pickle", "wb")
pickle.dump(dictionary, dictFile)