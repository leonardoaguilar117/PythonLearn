import math

# first definition


def factorial(n):
    def recurse(n, product):
        if n == 1:
            return product
        else:
            return factorial(n-1, n * product)
    recurse(n, 1)

# second definition
# of factorial


def factorial(n, product=1):
    if n == 1:
        return product
    else:
        factorial(n-1, n * product)


# A higher-order function is a function that receives another function as an argument and
# applies it in some way
oldList = [1, 2, 3, 4, 5, 6, 7, 8, 99, 32, 1, 34, 54, 1]
newList = []

for number in oldList:
    newList.append(str(number))


# Map function expects a function and an iterable object as arguments and returns anoter iterable object wheneir
# the argument function is applied to each iten contained

list_X = [4, 5, 7, 2, 55, 5, 2, 0]
squareOfList = list(map(lambda x: math.sqrt(x), list_X))
print(squareOfList)

# Alternatively, we can use filter function. This function expects a boolean function and an
# iterable object in wich each item is passed to the boolean function, if this function return
# true, the item is reteined in the returned iterable object; otherwise, the item is dropped from it

iterable = [- 7, 9, 6, -5, 99, 6, 77, -53]
newList = list(filter(lambda x: x > 0, iterable))
print(newList)
