# Exercise 1 : Use The Terminal
# Instructions
# Run this command in the terminal to open a python console:
# $ python3
# Hint: Replace python3 with python for Windows

# Read about the PATH variable. Try to explain why you can 
# call python3 if you aren’t in the executable directory.
# PATH explanation can be found here.


# a = True + 4
# b = False + 10

# print("a:", a)
# print("b:", b)


my_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum.'''

print(len(my_text))

# Exercise 5: Longest Word Without A Specific Character
# Instructions
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

a = 'a'

sentence = input('enter the longest sentence you can without the character A: ')
while a not in sentence: 
    sentence = input('enter the longest sentence you can without the character A: ')

i = 1
while i < 6:
  print(i)
  i += 1