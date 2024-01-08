""" Decorators in this case are way to declarate getter and setter function,
    they help us to obtain a attribute with any condicion or restriction
"""


class book:

    def __init__(self, title, ISBN, author):
        self.__title = title
        self.__ISBN_1 = ISBN
        self.__author = author

    # getter
    @property
    def ISBN(self):
        return self.__ISBN_1

    # setter
    @ISBN.setter
    def ISBN(self, ISBN):
        if ISBN.isdigit():
            self.__ISBN_1 = ISBN


if __name__ == "__main__":
    book_A = book("Three", 12314, "Mike")
    print(book_A.ISBN)
