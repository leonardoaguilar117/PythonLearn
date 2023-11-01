
"""Module providingFunction printing python version."""
phrase = input("Give me a word: ")
invertedPhrase = phrase[::-1]

if phrase == invertedPhrase:
    print("It´s a palindrome")
else:
    print("Is not a palindrome")
