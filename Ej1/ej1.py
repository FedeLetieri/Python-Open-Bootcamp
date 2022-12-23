#Enunciado: Imprime todos los ficheros existentes en tu carpeta de Descargas.
""" Obtén todos los ficheros y directorios de un directorio en concreto. Para ello necesitas una función existente 
en la librería os (Sistema Operativo) de Python.

Recorre todos los resultados obtenidos por la función anterior. Lo puedes hacer, por ejemplo, con un bucle for.

Imprime por pantalla solo aquellos resultados que sean ficheros (para ello también necesitas una función existente en os.

Ampliación:

Lista los tamaños de los ficheros en formato humano.

Recorre de manera recursiva todos los directorios desde tu carpeta personal y muestra los ficheros de cada directorio y su tamaño.
 """

import os
import pathlib
PATH = "C:\Downloads" #el path es la ruta de la carpeta Descargas
os.chdir(PATH)#Muevo el directorio a la carpeta de las descargas

#Recorre todos los resultados obtenidos por la función anterior. Lo puedes hacer, por ejemplo, con un bucle for.
archivos = os.listdir("{}".format(PATH))
#print(archivos) 

#Imprime por pantalla solo aquellos resultados que sean ficheros (para ello también necesitas una función existente en os.
with os.scandir(PATH) as ficheros:
    ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.txt')]

#Lista los tamaños de los ficheros en formato humano.
""" for fichero in ficheros:
    print(os.stat(fichero).st_size)
 """

#Recorre de manera recursiva todos los directorios desde tu carpeta personal y muestra los ficheros de cada directorio y su tamaño.
for archivo in archivos:
    print(archivo)
    print(os.stat(archivo).st_size)
