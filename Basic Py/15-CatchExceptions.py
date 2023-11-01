# When python encounters a semantic error, produce an exception and halts
# the program with an error message, so, for this, we have a try except statement


def safeIntegerInput(prompt):
    try:
        number = int(input(prompt))
        return number
    except ValueError:
        print("Error in number format")


if __name__ == "__main__":
    age = safeIntegerInput("Enter your age: ")
