# In cryptography, a Caesar cipher is one of the simplest and 
# most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in 
# the plaintext is replaced by a letter some fixed number of 
# positions down the alphabet.

# For example, with a left shift of 3, D would be replaced by A,
# E would become B, and so on. The method is named after Julius Caesar,
# who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages 
# with ceasar cypher, the user entries the program, 
# and then the program asks him if he wants to encrypt or 
# decrypt, and then execute encryption/decryption on a given 
# message and a given shift.
# tzhuw
# text = 'qwerty'

cypher_text = ""

init = input('would you like to encrypt or decrypt? ')

if init == 'encrypt':
    text_in = input('Please enter a sentence to encrypt: ')
    shift_in = int(input('How much do you want to shift? '))
    for letter in text_in:
        cypher_text += chr(ord(letter) + shift)
    
if init == 'decrypt':
    text_out = input('Please enter a sentence to decrypt: ')
    shift_out = int(input('How much do you want to shift? '))
    for letter in text_out:
        cypher_text += chr(ord(letter) - 3)

print(cypher_text)
