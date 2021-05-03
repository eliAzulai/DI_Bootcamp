# class Robot:
#     def __init__(self, name, color, ):
#         self.name = name 
#         self.color = color
#         self.weight = weight
    
#     def  introduce_self(self):
#         print(f'hi my name is {self.name}')
        
    
#     def rename(self,new_name):
#         self.name = new_name
     
# r1 = Robot('Tom', "red")
# r2 = Robot('jerry', 'Blue')

# r1.introduce_self()


# class Person():
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age

#   def show_details(self):
#       print("Hello my name is " + self.name)
    
#   def new_name(self, new_name):
#       self.name = new_name


# first_person = Person("John", 36)
# first_person.show_details()

# first_person.new_name('bob')
# first_person.show_details()

# Analyse the code below. What will be the output ?




# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    



# Exercise 1: Cats
# Instructions
# Using this class

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest 
# cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, 
# and is <cat_age> years old.”. Use the function previously created.
    # cats = []
    
    
    
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
        
# cat1 = Cat('tom', 5)
# cat2 = Cat('jim', 4)
# cat3 = Cat('bob', 3)

# all_cats = [cat1,cat2,cat3]

# def oldest_cat(all_cats):
#     current_oldest_cat = all_cats[0]
#     for cat in all_cats:
#         if cat.age > current_oldest_cat.age:
#              current_oldest_cat = cat
#     return cat
         
# oldest = oldest_cat(all_cats)
# print(f'The oldest cat is {oldest.name}, and is {oldest.age} years old.')

# Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height.
# This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”.
# x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
    
#     def bark(self):
#         print(f'{self.name} goes woof!')
    
#     def jump(self):
#         new_height = self.height * 2
#         print(f'{self.name} jumps {new_height} cm')
        
# davids_dog = Dog('Rex', 50)
# print(davids_dog.name)
# print(davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()

# saras_dog = Dog('Teacup', 20)
# print(saras_dog.name, saras_dog.height)
# saras_dog.bark()
# saras_dog.jump()

# all_dogs = [saras_dog, davids_dog]

# def find_biggest(all_dogs):
#         current_biggest_dog = all_dogs[0]
#         for dog in all_dogs:
#             if dog.height > current_biggest_dog.height:
#                 current_biggest_dog = dog
#         return dog 

# biggest = find_biggest(all_dogs)
# print(f'the biggest dog is {biggest.height} and name is called {biggest.name}')



# Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven



# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
        

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)


# song_lyrics = ["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"]
 
# stairway = Song(song_lyrics)

# stairway.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal.
# This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. 
# This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together 
# based on their first letter.
# 
animals = []

class Zoo:
    def __init__(self, name):
        self.animals = []
        self.name = name
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    
    def get_animals(self):
        print(self.animals)
        
    def sell_animals(self, animals_sold):
        if animals_sold in self.animals:
            self.animals.remove(animals_sold)
            
    def  sort_animals(self):
        animals_sorted = self.animals.sort()
        
    
       

lion1 = Zoo('london')
lion1.add_animal('lion')
lion1.add_animal('cheeta')
# lion1.sell_animals('cheeta')
# lion1.get_animals()
lion1.sort_animals()
lion1.get_animals()
    
        
        
# 
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

