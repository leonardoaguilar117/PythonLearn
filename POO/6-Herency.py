""" The superclass have methods and attributes that asigned to other classes, 
    depending on what is needed, in this case we have car class and two addicional classes
    ferrari and ibiza. They "inherit" characteristics of the superclass "car"
"""


class car:
    wheels = 4
    motor = True

    def __init__(self):
        pass

    def soundHorn(self):
        return "Peep"

    def accelerate(self):
        return "140 km/h"


class ferrari(car):
    def soundHorn(self):
        return "ranran" and super().soundHorn()


class ibiza(car):
    def soundHorn(self):
        return "ranran"
