#
# read binary file (tuple)
# and print it
#
#Para des-serializar el archivo
import pickle
#abre el archivo binario y lo asigna a la variable tup
with open('tupleFile.pickle', 'rb') as handle:
    tup = handle.read()
  
#Recronstrucción de la tupla
t = pickle.loads(tup)
#Impresión de los valores de la tupla obtenidos del archivo
print(t)