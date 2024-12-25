# Tokenization

string = input("Enter a string: ")
seperator = input("Enter a seperator: ")

tokens = string.split(seperator)

for token in tokens:
    print(token)
