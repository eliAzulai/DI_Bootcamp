# Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

# my_fav_numbers = {1,3,4,5,53}
# my_fav_numbers.update([66,2])
# my_fav_numbers.remove(2)

# friend_fav_numbers = {7, 65, 33}
# our_fav_numbers = set.union(friend_fav_numbers, my_fav_numbers)
# print(our_fav_numbers)



# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# no


# Exercise 3: Print A Range Of Numbers
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.

# numbers = range(1,21)

# for number in numbers: 
#     print(number)

# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# numbers = range(1.5, 5, 0.5)
# print(numbers)

# Exercise 5: Shopping List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.pop(0)
# basket.pop(2)
# basket.append('Kiwi')
# basket.insert(0, 'Apples')
# count_apples = basket.count("Apples")
# basket.clear()
# print(basket)


# Exercise 6 : Loop
# Instructions
# Write a while loop that will continuously ask the user
# for their name, unless the input is equal to your name.

# ask = ''
# my_name = 'eli'

# while ask != my_name:
#     ask = input('whats your name? ')
# print('We have the same name')

# Exercise 7
# Instructions
# Given a list, use a loop to print out every 
# element which has an even index.

# numbers = (1,2,3,5)

# for idx, num in enumerate(numbers):
#     if (idx % 2 ) == 0:
#         print(idx, num)


    
    
# Exercise 8
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.



# for numbers in range(1500, 2501):
#     if (numbers % 5) == 0 or (numbers % 7) == 0:
#         print(numbers)

# Exercise 9: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate 
# the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words 
# into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of 
# your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope 
# you enjoy”.\
    
# fav = input('enter your fav fruit or fruits seperated with a single space ')

# fav_list = fav.split()

# new_fruit = input('enter a new fruit: ')

# for fruit in fav_list: 
#     if new_fruit == fruit:
#         print('you choose a favourite fruit')
#     else: ('you chose a new fruit') 

#
# 
# 
# Exercise 10: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, 
# when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping 
# to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total 
# price is (10 + 2.5 for each topping).

# i = 1
# while True:
#     print(i)
#     i = i + 1
#     if(i > 3):
#         break

pizza_top = []

while pizza_top != 'quit':
    pizza_top = input('What would you like on your pizza? (type quit when you are done):')
    pizza_sofar = [pizza_top]
    print(pizza_sofar)

    
# Exercise 11: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want to watch a movie 
# that is restricted for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints a list of the
# teens who are permitted to watch the movie.



# Exercise 12 : Who Is Under 16?
# Instructions
# Given a list of names, write a program that asks every user for their age, 
# if they are less than 16 years old remove them from the list.
# At the end, print the final list.


# Exercise 13
# Instructions
# Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made ,
# such as I made your tuna sandwich.


# Exercise 14
# Instructions
# Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ 
# appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of 
# pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.