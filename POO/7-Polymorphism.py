from abc import ABC, abstractclassmethod


class Model(ABC):

    @abstractclassmethod
    def guardar(self):
        pass


class User(Model):
    def guardar(self):
        print("Guardado")


class Sesion(Model):
    def guardar(self):
        print("Guardando archivo")
