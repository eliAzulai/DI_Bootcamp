# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:

#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, 
# then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes 


birthday = input('please enter your birthday in format DD/MM/YYYY: ')
bday = birthday.split('/')
bday_year = int(bday[2])

date_today = '06/05/2021'
date_today_list = date_today.split('/')
date_year = int(date_today_list[2])

age = date_year - bday_year
# print(age)

last_digit = str(age)
last_digit = list(last_digit)
last_digit = int(last_digit[1])

if last_digit == 0:
    print('well done you get 10 candles')
    last_digit += 10
    
# print(last_digit)

cake = '''
       _____i_____
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~

'''
cake_without_top = '''
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~

'''

candles = last_digit * 'i'
candles = candles.center(11, '_')

index = cake.find('_____i_____')
cake_output = cake[:index] + candles + cake_without_top 
print(cake_output)