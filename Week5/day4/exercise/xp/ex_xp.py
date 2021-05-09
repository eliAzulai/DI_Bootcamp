# Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. 
# We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words 
# as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. 
# The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:
# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. 
# Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

import random

def get_words_from_file():
    sowpods = open('/Users/Azulai/Dropbox/Developers_Institute/Week5/day4/exercise/xp/sowpods.txt')
    sow_list = sowpods.readlines()
    return sow_list
    # print(sow_list)
    
sow_list = get_words_from_file()
    

def get_random_sentence(length):
    random_sentence = []
    while length > 0:
        random_word = random.choice(sow_list)
        random_sentence.append(random_word)
        length -= 1
    return random_sentence
        
random_sentence = get_random_sentence(5)

for i in range(len(random_sentence)):
    random_sentence[i] = random_sentence[i].lower()

print(random_sentence)
    
         
def input_validation():    
    while True:
        try:
            length = int(input('How long do you want the sentence to be, please enter a number between 2 and 20: '))
        except:    
            print('please enter numeric digits')
        if length > 20:
            print('Please enter a number below 20')
        elif length < 3:
            print('please enter a number above 3')
        break    
    return length
         
input_validation()          
            
def main():
    print('This program takes a text file and imports it, turning it into a list of strings. Then the a number is given as to the length of the sentence that is genrated at ranodom from the list of strings. Then the sentence is turned into lower case')

main()

# Exercise 2: Working With JSON
# Instructions
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

# import json

# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
