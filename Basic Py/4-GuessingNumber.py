"""Plays a gamme of guess the number"""
import random

def main():
    smaller = int(input("Enter the smaller number:"))
    larger = int(input("Enter the larger number: "))
    my_Number = random.randint(smaller, larger)
    count = 0

    while True:
        count += 1
        userNumber = int(input("Enter a number: "))
        if userNumber < my_Number:
            print("Too small")
        elif userNumber > my_Number:
            print("Too large")
        else:
            print("You´ve got it")
            break


main()
