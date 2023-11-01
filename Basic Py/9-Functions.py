import shutil
import random

# Función que nos permite eliminar una ruta especificada


def deletePath(Url):
    if Url > 1:
        shutil.rmtree(Url)
        return print(f"Ruta{Url} eliminada")
    else:
        return print(f"La ruta {Url} no fue eliminada")


# xargs, nos permiten meter varios argumentos dentro de una funcion
def concatenates(*string):
    finalString = ""
    for word in string:
        finalString += " "+word
    return finalString

# kwargs son funciones que reciben dentro de sus parametros variables con un valor especifico


def ejemplo_funcion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
