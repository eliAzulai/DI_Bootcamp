# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message 
# congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 
# 18 and 
# False if not.
# a method that prints all the members of the family.
        

class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name
  
    def show_members(self):
        print (self.members)

    def born(self, **kwargs):
        self.members.append(kwargs)
        print('congratulations')
    
    def is_18(self, other):
        for key, value in other.items(): 
            if value > 18:
                return True
            else:
                return False
    
members =[
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]   
    
family = Family(members,'Jones')
                
michael.show_members()
michael.born(name='Fred',age=0,gender='Male',is_child=True)

# michael.show_members()

print(michael)
michael.is_18(michael)

# Exercise 2 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore we need to add the following 
# keys to our dictionaries: power and incredible_name.

# Add a method called use_power, this method should print the power of a member if they are over 18 years old.
# If not raise an exception (look up exceptions) which stated they are not over 18 years old.

# Add a method called incredible_presentation which presents the family members with their incredible names and
# powers.

# Look up the names of The Incredibles characters on Google and build the family (if you can’t find the correct
# information just improvise).
# Print their normal presentation and their incredible presentation.
# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# Print both presentations again. Check that Baby Jack is born and that his power is showing when using the incredible 
# representation.

# class TheIncredibles(Family):
    
    def add_inc_power():
        
        
#         d = {'key': 'value'}
# print(d)
# # {'key': 'value'}
# d['mynewkey'] = 'mynewvalue'
# print(d)
# # {'key': 'value', 'mynewkey': 'mynewvalue'}    
    