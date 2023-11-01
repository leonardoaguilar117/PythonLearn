class Bass:
    # The objects have particular characteristics, that is why we can puts attributes for all
    # instances of this class
    strings = "Niquel"
    color = "red"

    def __init__(self, name, brand, numbString):
        self.name = name
        self.brand = brand
        self.numbString = numbString

    def showCharacteristics(self):
        print(
            f"Brand: {self.brand}, Name of bass: {self.name}, Number of strings: {self.numbString}")

    # A classmethod is a way to initializate a instance with a default setting
    @classmethod
    def factorySet(cls):
        return Bass("Unknown", "Mos", 4)


if __name__ == "__main__":
    Spector = Bass("Specto bass", "Spector", 5)
    Spector.showCharacteristics()

    # Adicionaly: we can change values of attributes from main function
    # Have two ways: from the class or from instance
    # for example:

    Bass.color = "Blue"
    # If we change bass color from the class, all new instances they will have this color

    Spector.color = "Black"
    # On the other hand if we change the attribute from the instance, will only change in this

    Warwick = Bass.factorySet()
    Warwick.showCharacteristics()
