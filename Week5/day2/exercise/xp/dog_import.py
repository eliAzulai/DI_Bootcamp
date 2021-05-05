# Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be 
# False by default.
# Add the following methods:train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other dogs (use *args). 
# The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

from exercise_xp import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False      
    
    def train(self):
        self.bark()
        return self.trained == True
        
    def play(self, *args):
        dogs = ', '.join(args)
        print(f"the dogs: {dogs} play together")
        return self.trained == False
        
    def do_a_trick(self, *args):
        trick_number = random.randint(0, 3)
        if self.trained == True:
            if trick_number == 0:
                print(f'{args.name} does a barrel roll')
                args.trained = False
            elif trick_number == 1:
                print(f'{args.name} stands on his back legs')
                args.trained = False
            elif trick_number == 2:
                print(f'{args.name} stands on his back legs')
                args.trained = False
            else:
                print(f'{args.name} plays dead')
                args.trained = False
    
    
dog1 = PetDog('Tom', 12, 6)
dog2 = PetDog('Rocky', 3, 3)
dog3 = PetDog('Flossy', 5, 4)

dog1.train()
# dog2.play('Flossy','rocky')
dog3.do_a_trick('flossy')