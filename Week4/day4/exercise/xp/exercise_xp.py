# Write a function calculation() such that it can accept 
# two variables and calculate the addition and subtraction of it. 
# And also it must return both addition and subtraction in a single return call

# def calculation(a, b):
#     c = a - b
#     d = a + b
#     return c,d

# res = calculation(40, 10)
# print(res)

# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints 
# one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.



# def display_message():
#     print('I am learning Python functions')
    
# display_message()




# Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as “One of my favorite books is
# Alice in Wonderland”.
# Call the function, make sure to include a book title as an argument when 
# calling the function.

# def favorite_book(title):
#     print(f'One of my favorite books is {title}')
      
# favorite_book('Alice in Wonderland')


# Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and 
# its country as parameters.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the country parameter a default value.
# Call your function.




# def describe_city(city, country):
#     print(f'{city} is in {country}')

# describe_city('Reykjavik', 'Iceland')

    

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another 
# number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message,
# otherwise show a fail message and display both numbers.


# from random import randint

# def ran_number():
#     ran_ask = int(input(f'please enter a random number between 1 - 100: '))
#     ran = randint(0, 100)
#     if ran == ran_ask:
#         print('SUCCESS')
#     else: print(f'FAIL your random number was {ran_ask} and the randomly generated number was {ran}')
    
# ran_number()


# Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a 
# message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and 
# the message printed on it.
# Call the function make_shirt() using positional arguments to make a shirt.
# Modify the make_shirt() function so that shirts are large by default with a message
# that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any 
# size with a different message.
# Bonus: Call the function make_shirt() using keyword arguments.

# def make_shirt(size = 'large', text = 'I love python'):
#     print(f'The size of your shirt is {size} and the message is {text}')
    
# make_shirt()
# make_shirt('medium', 'I love Python')
# make_shirt('small', 'I love Python')

# Exercise 6 : Magicians …
# Instructions
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of
# each magician in the list.
# Write a function called make_great() that modifies the list of magicians by 
# adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

magicians = ['Maldred', 'Merlin', 'Snape']

# def show_magicians(*args):
#     print(*args)
    
# show_magicians(magicians)

# def make_great():
#     mag_great = [mag + ' The Great' for mag in magicians]
#     print(mag_great)
    
# make_great()


magicians = ['Maldred', 'Merlin', 'Snape']

def show_magicians(*args):
    print(*args)
    
show_magicians(magicians)

def make_great():
    for key,mag in enumerate(magicians):
	    magicians[key] = mag + ' The Great'

    print(magicians)
    
make_great()

show_magicians(magicians)