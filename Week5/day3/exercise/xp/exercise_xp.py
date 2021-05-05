# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a 
# look at the python documentation online.

# Write a program which prints some of python’s built-in functions such 
# as abs(), int(), raw_input().
# Write a documentation for your newly created function.

# Create your own documentation explaining what your classes functionality is, 
# you can do this by using the __doc__ dunder method take a look on google for help.

# class Example:
#     ''' This is my doc string, it describes my class which is just a simple addition'''
#     def __init__(self):
#         self.number_x = abs(int(input('please enter a number: ')))
#         self.number_y = abs(int(input('please enter a number: ')))
    
#     def sum():
#         result = self.number_x + self.number_y
#         return result

# print(Example.__doc__)
    




# Exercise 2: Currencies
# Instructions
# Create the code which will output the results below.
# Hint : When adding 2 currencies which don’t share 
# the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c4 = Currency('shekel', 1)
# >>> c3 = Currency('shekel', 10)

# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1 
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>

class Currency:
    def __init__(self, currency_type, amount):
        self.currency_type = currency_type
        self.amount = amount
    
    def __str__(self):
        return f'{self.amount} {self.currency_type}s'

    def __int__(self): 
        return self.amount
    
    def __repr__(self):
        return f'{self.amount} {self.currency_type}s'
    
    def __add__(self, second):
        if self.currency_type != second.currency_type:
            print('TypeError: Cannot add between Currency type <dollar> and <shekel>')
        else:
             self.amount += int(second)
        return f'{self.amount} {self.currency_type}s'


    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c4 = Currency('shekel', 1)
c3 = Currency('shekel', 10)


# print(str(c1))
# print(int(c1))
# print(repr(c1))
# print(str(c1.amount + 5))
# print(c1 + c2)
# print(c1)

# c1 += 5
# print(c1)

# c1 += c2
# print(c1)

print(c1 + c3)
