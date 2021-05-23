# Exercise 3: Print A Range Of Numbers
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.

# counter = 1
# while counter != 21:
#     print(counter)
#     counter +=1


# Exercise 6 : Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, 
# unless the input is equal to your name.

# name = ''
# my_name = 'eli'


# while name != my_name:
#     name = input(f'what is your name: ')
    
    
# Exercise 7
# Instructions
# Given a list, use a loop to print out every element which has an even index.

# given_list = ['e','r','t','w','s','f']

# for i in given_list:
#     if given_list.index(i) %2 == 0: 
#         print(i)

# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

# for i in range(1499, 2501):
#     if i % 7 == 0:
#         print(i)
#     if i % 5 == 0:
#         print(i)

# Exercise 9: Favorite Fruits

# 1.Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# 2.Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# 3. Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# fav_fruit = []

# counter = 0 

# while True: 
#     fav_fruit = input(f'please input fav fruit with comma seperated: ')
#     fav_fruit_list = fav_fruit.split(',')
#     chosen_fruit = input(f'tell me a fruit that you picked: ')
    
    
#     if fav_fruit_list[counter] == chosen_fruit:
#         print('you chose one of your fav fruits!')
#         break
    
#     else:
#         print('you chose a differnet fruit enjoy')
#     counter +=1

    
# Exercise 10: Who Ordered A Pizza ?
# Instructions
# 1 Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# 2 As they enter each topping, print a message saying you’ll add that topping to their pizza.
# 3 Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).


# pizza_toppings = []
# active = True
# cost = 10

# while active: 
#     pizza_topping = input('enter your pizza topping: ')
#     if pizza_topping != 'quit':
#         print(f'i added {pizza_topping} to your pizza')
#         pizza_toppings.append(pizza_topping)
#         cost += 2.5
#     else:
#         active = False

# print(f'your pizza costs {cost} and has these {pizza_toppings} toppings')


# Exercise 11: Cinemax
# Instructions
# 1. A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# 2. Ask a family the age of each person who wants a ticket.
# 3. Store the total cost of all the family’s tickets and print it out.
# 4. A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie.


# active = True
# cost = 0

# while active: 
#     age = input(f'what is your age of each person who wants a ticket? ')
#     if age != 'quit': 
#         if int(age) >= 3 and int(age) <= 12: 
#             cost += 10 
#         if int(age) > 12:
#             cost += 15    
#         if int(age) < 3:
#             cost += 0
#     else:
#         active = False 
# print(cost)

    

# if age >= 16 and age <= 21: 
    

    
# Exercise 12 : Who Is Under 16?
# Instructions
# 1. Given a list of names, write a program that asks every user for their age, 
# if they are less than 16 years old remove them from the list.
# 2. At the end, print the final list.
    
# people = ['john','benny', 'toby', 'smith', 'sandra']
# active = True
# counter = 0

# while active: 
#     age = int(input(f'what is your age {people[counter]}? '))
#     if age < 16: 
#         people.remove(people[counter])
#     counter += 1 
#     if counter > len(people):
#         active = False

# print(people)

# //////// using a for loop

# people = ['john','benny', 'toby', 'smith', 'sandra']
# people_sorted = []

# for individual in people: 
#     age = int(input(f'what is your age {individual}? '))
#     if age > 16:
#         people_sorted.append(individual)
# print(people_sorted)
    

# Exercise 13
# Instructions
# 1. Make a list called sandwich_orders and fill it with the names of various sandwiches .
# 2. Then make an empty list called finished_sandwiches.
# 3. As each sandwich is made, move it to the list of finished sandwiches.
# 4. After all the sandwiches have been made, print a message listing each sandwich that was made , 
# such as I made your tuna sandwich.

# sandwhich_orders = ['tuna', 'radish', 'cheese']
# finsihed_sandwhiches = []
# active = True 
# counter = 0 

# while active:
#     finsihed_sandwhiches.append(sandwhich_orders[counter])
    
#     counter += 1 
#     if counter == len(sandwhich_orders):
#         active = False

# print(finsihed_sandwhiches)

# Exercise 14
# Instructions
# Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
# and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

# USING A WHILE LOOP/////////////

# sandwhich_orders = ['tuna', 'pastrami','radish','pastrami', 'cheese', 'pastrami', 'pastrami']

# sadwhich_without_pastrami = []

# active = True

# print(f'sorry the deli has run out of pastrami')

# while active: 
#     for i in sandwhich_orders:
#         if i != 'pastrami':
#             index = sandwhich_orders.index(i)
#             sadwhich_without_pastrami.append(sandwhich_orders[index])
#         else:
#             active = False
            
# print(sadwhich_without_pastrami)

# EASIER WAY WITH FOR LOOP
# sandwhich_orders = ['tuna', 'pastrami','radish','pastrami', 'cheese', 'pastrami', 'pastrami']

# sadwhich_without_pastrami = []

# for sandwhich in sandwhich_orders: 
#     if sandwhich != 'pastrami':
#         sadwhich_without_pastrami.append(sandwhich)
# print(sadwhich_without_pastrami)



# def hello(*kwargs):
#     print(kwargs)

# hello(firstname = 'chaim', lastname = 'martin')

# class Vehicle:
#     def __init__(self, vehicle_type):
#         self.vehicle_type = vehicle_type
#         self.parts = []
#         self.col = ''
#         self.engine = ''
        
#     def tires(self, amount):
#         amount_of_tires = f'{amount} tires'
#         self.parts.append(amount_of_tires)
        
#     def choose_colour(self, colour):
#         colour = f'your vehicles is color {colour}'
#         self.col = colour
        
#     def body(self):
#         if self.vehicle_type == 'car':
#             self.parts.append('car body')
#         elif self.vehicle_type == 'truck':
#             self.parts.append('truck body')
#         elif self.vehicle_type == 'motorcycle':
#             self.parts.append('motorcycle body')
#         elif self.vehicle_type == 'plane':
#             self.parts.append('plane body')
            
#     def display(self):
#         print(f'Parts needed to build your {self.vehicle_type}')
#         for part in self.parts:
#             print(f'{self.parts.index(part) + 1}: {part}')
    
#     def choose_engine(self, engine_type):
#         engine_type = f'your vehicle has engine {engine_type}'
#         self.engine = engine_type
        
            
#     def __repr__(self):
#         return f'type: {self.vehicle_type} parts: {self.parts}'
    
# v1 = Vehicle('car')
# v2 = Vehicle('motorcycle')
# v3 = Vehicle('plane')

# v1.tires(4)
# v1.choose_colour('blue')
# print(v1.col)
# v1.choose_engine('v8')
# print(v1.engine)


# class SuperList(list):
#     def __len__(self):
#         return 1000
  

# super_list1 = SuperList()
# print(len(super_list1))

# super_list1.append(5)
# print(super_list1[0])
# print(issubclass(SuperList, list))


# class Cat:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
    
#     def eat(self):
#         print(f'{self.name} is now eating')
        
#     def jump(self):
#         print(f'{self.name} is now jumping')
        
#     def play(self):
#         print(f'{self.name} is now playing')
        
# class TypeCat(Cat):
#     def __init__(self, name, color, fur_type):
#          super().__init__(name, color)
#          self.fur_type = fur_type
         
#     def __repr__(self):
#         return f'{self.name} is {self.color} and is fur type {self.fur_type}'

    
# c1 = TypeCat('toby', 'blue', 'shaggy')
# print(c1)

# c1.jump()

counter = 0
my_list = [1,2,3,4,5,6,7,8,9,10]

for item in my_list:
    counter = counter + item

print(counter)