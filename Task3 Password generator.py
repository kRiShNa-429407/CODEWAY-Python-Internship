## Import random module for random set of characters:

import random

## Define password length  you want:

password_length = int(input("Enter the length of password\n"))

 ## Make a strings of character you want to use in your password:

characters = "abcde12345@#$!&"

password = ""     ## create an empty string of password

## Run for loop to iterate over your password lenght:

for index in range(password_length):
    password = password + random.choice(characters)

print("Password generated: {}".format(password))