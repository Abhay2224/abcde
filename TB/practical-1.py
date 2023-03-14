#Write a program for tokenization of given input in python
import re

my_text=input("Enter a string for tokenization ")

my_token = my_text.split(',',1)

print('Tokenization of given input: ')
print(my_token)

# ----------------------------------------------------------------------------------------

my_text1 = input("Enter a string for tokenization: ")

print("Tokenization of given input: ")
pattern = re.compile('\w+')
matches = pattern.finditer(my_text1)
for token in matches:
    print(token) 

# -------------------------------------------------------------------------------------------

# Write a program for tokenization of given input in python

import tokenize

with tokenize.open("practical-1.py") as f:
    tokens = tokenize.generate_tokens(f.readline)
    for token in tokens:
        print(token)