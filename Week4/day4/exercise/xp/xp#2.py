# Exercise 7: When Will I Retire ?
# Instructions
# The point of the exercise is to check if a person can 
# retire depending on their age and their gender.
# Note : Retirement age in Israel is 67 for men, and 62 for women (
# born after April, 1947).

# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing 
# this, but for now it will be enough.)
# After calculating the age of a person, the function should return the age 
# (the age is an integer).
# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age.
# Now it has all the information it needs in order to determine if the person with the given 
# gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.
# Some Hints
# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message informing the user whether they can retire or not.
# As always, test your code to ensure it works.
year = 2021
month = 4

def get_age(year = 2021, month = 4,):
    input_year = input('Please enter the year you were born: ')
    input_month = input('Please enter the month you were born: ')
    age = input_year -
    # print(input_age) 

get_age()



# Exercise 8:
# Instructions
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:

# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)
# Hint: treating our number as a int or a str at different points in our code may be helpful