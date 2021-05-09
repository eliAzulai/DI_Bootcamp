# Daily Challenge - Circle
# Last updated : May 3rd 2021
# What You Will Learn :
# OOP
# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them

class Circle:
    def __init__(self, radius, diameter):
        self.radius = radius
        self.diameter = diameter