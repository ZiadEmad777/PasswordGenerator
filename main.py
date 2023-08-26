######################################################################################
# Project Name : Password Generator
# File Name    : main.py
# Author       : Ziad Emad
# Date         : 26 Aug 2023
#######################################################################################
import random


def shuffle(random_password):
    temp_list = list(random_password)
    random.shuffle(temp_list)
    return temp_list


print("Welcome To Password Generator program 2023")
print("Generating password will be composed of 2 Uppercase letters")
print("Generating password will be composed of 2 Lowercase letters")
print("Generating password will be composed of 2 Digits")
print("Generating password will be composed of 2 Punctuation sign")
print(" ")

# Entering 2 upper case letters to generate the password
upper_caseLetter1 = chr(random.randint(65, 90))
upper_caseLetter2 = chr(random.randint(65, 90))

# Entering 2 lower case letters to generate the password
lower_caseLetter1 = chr(random.randint(97, 122))
lower_caseLetter2 = chr(random.randint(97, 122))

# Entering 2 digits to generate the password
digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))

# Entering 2 Punctuation Signs to generate the password
punctuationSign1 = chr(random.randint(33, 152))
punctuationSign2 = chr(random.randint(33, 152))

# Create a variable to store the password in it in random way
password = (upper_caseLetter1 + upper_caseLetter2 +
            lower_caseLetter1 + lower_caseLetter2 + digit1 + digit2
            + punctuationSign1 + punctuationSign2)

password = shuffle(password)
# showing the password for the program user
print("The Password is:")
for i in range(8):
    print(password[i], end="")
