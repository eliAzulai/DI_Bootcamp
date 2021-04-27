# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

# Then, print the first and last characters of the given text.




user_input = input('Enter sentence here exactly 10 characters long: ')
if (len(user_input)) < 10:
    print("string not long enough")
elif (len(user_input)) > 10 :
    print('string too long')
else: print(user_input[0],user_input[9])


# Construct the string character by character: Print the first character, then the second, 
# then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World

print (user_input[0] + "\n")
print (user_input[0:1] + "\n")
print (user_input[0:2] + "\n")
print (user_input[0:3] + "\n")
print (user_input[0:4] + "\n")
print (user_input[0:5] + "\n")
print (user_input[0:6] + "\n")
print (user_input[0:7] + "\n")
print (user_input[0:8] + "\n")
print (user_input[0:9] + "\n")


# 4. Swap some characters around then print the newly jumbled string 
# (hint: look into the shuffle method). For example:

# Hlrolelwod

# qwertyuiop

user_input = user_input.split(' ')


import random

random.shuffle(user_input)

print(user_input)

# import random
# l = user_input
# random.shuffle(l)
# result = ''.join(l)

