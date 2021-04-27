# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# keysToRemove = ["name", "salary"]

# for key in keysToRemove: 
#     del sampleDict[key]
    
# print(sampleDict)


# Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# for t in zip(keys,values):
#     print(t)
    
    
# Exercise 2 : Cinemax #2
# Instructions
# “Continuation of Exercise Cinemax from Week4Day2 XP”

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided 
# family variable (Hint: ask the user for names and ages and add them into a family 
#  dictionary that is initially empty).

# family = {"rick": 43}, 'beth': 13, 'morty': 5, 'summer': 8}
# total_cost = 0

# for person, age in family.items():
#     if age < 3:
#         total_cost = 0
#         print(f' {person} has to pay {total_cost}')
#     elif age >= 3 and age <= 12:
#         total_cost += 10
#         print(f' {person} has to pay {total_cost}')   
#     else:
#         total_cost += 15
#         print(f' {person} has to pay {total_cost}')   
# print(f'the family has to pay {total_cost}$')    
        
        
# Here is some information about a brand.

# 2. Create a dictionary called brand which value is the information from part one 
# (turn the info into keys and values).
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.


brand = {'name': 'Zara', 
         'creation_date': 1975, 
         'creator_name': 'Amancio Ortega Gaona', 
         'type_of_clothes': [
             'men', 'women', 'children', 'home'
             ], 
            'international_competitors': ['Gap', 'H&M', 'Benetton'], 
         'number_stores': 7000, 
         'major_color': 
             {'France': 'blue', 
              'Spain': 'red', 
              'US': ['pink', 'green']
     }
}

brand['number_stores'] = 2
print('Zaras clients are any man or woman who wears clothes')
brand['country_creation'] = 'Spain'
if brand['international_competitors']:
    brand['internatinol_competitros'] = 'Desigual'

del brand['creation_date']

# print(brand['international_competitors'][2])
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.

# print(brand['major_color']['US'][0], brand['major_color']['US'][1])

# print(len(brand))

# for key in brand:
#     print(key)


# 12. Create another dictionary called more_on_zara with the following details:

more_on_zara = {'creation_date': 1975, 
'number_stores': 10000
}

brand.update(more_on_zara)
# print(brand)
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?

print(brand['number_stores'])

# It got updated with the value from the second dict



# Exercise 4 : Disney Characters
# Instructions
# Use this list :

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# Analyse these results :

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# next = 1

# users_dict = dict.fromkeys(users, 0)
# print(users_dict)

# for key, value in users_dict.items():
#     users_dict[key] = next
#     next +=1
# print(users_dict)
 

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# new_dict = dict()
# key = 0
# inc = 0

# for user in users:
#     new_dict.setdefault(key)
#     new_dict[key] = users[inc]
#     inc +=1
#     key +=1
# print(new_dict)    
 

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
users.sort()
user_dict = dict()
value = 0

for user in users:
    user_dict[user] = value
    value += 1
print(user_dict)

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.