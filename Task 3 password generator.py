import string
import random

def generate_password(length, complexity):
    letters = string.ascii_letters
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation

    characters = letters
    password = ""

    if complexity == "1":
        has_lowercase = False
        has_upperCase = False
        criteria = False

        while not criteria or len(password) < int(length):
            new_char = random.choice(letters)
            password += new_char

            if new_char in lower_letters:
                has_lowercase = True
            elif new_char in upper_letters:
                has_upperCase = True
            
            criteria = has_upperCase and has_lowercase
    
    elif complexity == "2":
        has_letters = False
        has_digits = False
        criteria = False

        characters += digits

        while not criteria or len(password) < int(length):
            new_char = random.choice(characters)
            password += new_char

            if new_char in letters:
                has_letters = True
            elif new_char in digits:
                has_digits = True
            
            criteria = has_letters and has_digits


    elif complexity == "3":
        has_letters = False
        has_digits = False
        has_punctuation = False
        criteria = False

        characters += digits
        characters += punctuation

        while not criteria or len(password) < int(length):
            new_char = random.choice(characters)
            password += new_char

            if new_char in digits:
                has_digits = True
            elif new_char in punctuation:
                has_punctuation = True
            
            criteria = has_digits and has_punctuation
    
    else:
        return "Please Enter a complexity level from 1 to 3"

    return password

quit = ""

while quit == "" or quit == "y":
    length = input("Enter the length of password: ")
    complexity = input("Enter the lvl of complexity from 1 to 3: ")
    print(generate_password(length, complexity))

    quit = input("Do you want to generate another Password(y/n): ").lower()

