import os
import sys
import platform
import random
var = "ola"

# Básicos
print(os.getcwd())  # impresión de la ruta actual

os.chdir("C:/Users/leona/Downloads/Arqui")  # Cambio de ruta

print(os.listdir())  # Muestra los directorios y archivos de esa ruta

os.mkdir("Prueba")  # Crear directorio
print(os.listdir())

os.makedirs("dir")  # Crear directorios

os.rmdir("Prueba")  # Eliminar directorio

os.remove("archivo")  # Elimina un archivo especifico

os.rename("src", "name")  # Cambia el nombre del directorio en ruta

os.path.exists("path")  # Devuelve true si la ruta existe

os.system("instrucción")  # Realiza una instrucción en la consola

# f es un format string que indica que dentro de un string se
os.system(f"{var} ")
# implementarán variables {} para crear un string

os.name == "ce" or os.name == "nt" or os.name == "dos"
os.name == "posix" or os.name == "mac"
# Podemos usar esta sentencia para indicar que una instrucción se va a ejecutar en dicho SO

