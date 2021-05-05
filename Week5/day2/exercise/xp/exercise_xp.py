
    
    
# class Door:
#     def __init__(self, is_opened):
#         self.is_opened = is_opened
        
#     def open_door():
#         self.is_opened = True
        
#     def close_door():
#         self.is_opened = False
    
# class BlockedDoor(Door):
#     def open_door():
#          self.is_opened = False
         
#     def close_door():
#         self.is_opened = False
    
# my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

# def return_list(given_list):
#     total = 0 
#     for num in given_list:
#         try:
#             total += int(num)
#         except: 
#             num = 0
             
#     return total

# print(return_list(my_list))
    



# Exercise 1 : Pets
# Instructions
# Using this code:
# Create another cat bread. In order to do so, create a class which inherits from 
# the Cat class.
# Create a few cat instances.
# Create a list called my_cats, which will hold all the created cat instances.
# Create a variable called my_pets. It’s value is an instance of the Pet class.
# Hint : Use the my_cats variable to create the instance.
# Take all the cats for a walk, use the walk method.


# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Syamiese(Cat):
#     pass

# cat1 = Syamiese('tom', 24)
# cat2 = Bengal('rad', 24)
# cat3 = Chartreux('garfield', 24)

# all_cats = [cat1, cat2, cat3]
# my_pets = Pets(all_cats)
# my_pets.walk()

# Create a variable called my_pets. It’s value is an instance of the Pet class.
# Hint : Use the my_cats variable to create the instance.
# Take all the cats for a walk, use the walk method.


# Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value should be another dog 
# called other_dog, 
# returns a string stating which dog won the fight. 
# The winner should be the dog with the higher run_speed x weight.


class Dog: 
    def __init__(self, name, age, weight):
        self.name = name 
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f'{self.name} is barking'
    
    def run_speed(self):
        running_speed = self.weight / (self.age * 10)
        return running_speed
    
    def fight(self, other_dog):
        running_speed = self.run_speed()
        if running_speed * self.weight > other_dog.run_speed() * other_dog.weight:
            print(f'The dog that won is {self.name}') 
        else:
            print(f'the dog that won is {other_dog.name}')

            
        return f'The dog that won is {self.name}'      

dog1 = Dog('Tom', 12, 6)
dog2 = Dog('Rocky', 3, 3)
dog3 = Dog('Flossy', 5, 4)


dog3.fight(dog2)
dog1.fight(dog2)
dog2.fight(dog3)





# Create 3 dogs and run them through your class.


# Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other dogs (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.


