#
# read binary file (dictionary)
# and print it
#
#Para des-serializar el archivo
import pickle
#abre el archivo binario y lo asigna a la variable dictionary
with open('dictFile.pickle', 'rb') as handle:
    dictionary = handle.read()
  
#Recronstrucción del diccionario
d = pickle.loads(dictionary)
#Impresión de los valores del diccionario obtenidos del archivo
print(d)