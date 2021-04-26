user = input('Give me a number between 1 and 100: ')
integer = int(user)
if integer % 3 == 0 and % 5 == 0:
 print ('FizzBuzz')
elif integer % 3 == 0:
    print ('Fizz')
elif integer % 5 == 0:
    print ('Buzz')
