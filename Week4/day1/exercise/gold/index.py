# Exercise 1 : Hello World-I Love Python
# Instructions
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python

print('Hello World\n' * 4,'I love python\n' * 4)

# Exercise 2 : What Is The Season ?
# Instructions
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)


random_month = int(input("enter a month 1-12: "))
if random_month > 0 and random_month <= 2 or random_month == 12:
    print('the season is winter')
elif random_month >= 3 and random_month <= 5: 
    print('the season is spring')
elif random_month >=6 and random_month <= 8:
    print('the season is summer')
elif random_month >=9 and random_month <=11:
    print('the season is autumn')
    
    