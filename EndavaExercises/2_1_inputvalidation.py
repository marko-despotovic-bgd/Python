# 2. Conditionals
# 1.1. Write a console program that asks user for name, surname and age. After
# input is provided, program prints two different outputs sequentially:
# Name: <name>
# Surname: <surname>
# Age: <age>
# 2.1. Add basic input validation in tasks from exercise (1). If input is
# invalid (for example, an empty string is provided), print appropriate message.


print('Please enter Name, Surname and Age: ')
name = input('Name: ')
if name:
    surname = input('Surname: ')
    if not surname:
        print('You did not entered valid surname!')
    else:
        age = int(input('Age: '))
        if age <= 0:
            print('You did not entered valid age!')
        else:
            print('Person {0} {1} is {2} years old.'.format(name, surname, age))
            print('Person {} {} is {} years old.'.format(name, surname, age))

else:
    print('You did not entered valid  name!')


# Write a console program that asks for a string and outputs string length
# as well as first and last three characters.
# Add basic input validation in tasks from exercise (1). If input is invalid
# (for example, an empty string is provided), print appropriate message.

#1.3
print('Please enter some string: ')
string = (input())

if string:
    print('Length: {}\nFirst 3 chars: {}\nLast 3 chars: {}'.format(len(
        string),
        string[:3],
        string[-3::1]))
else:
    print('You did not enter valid string')
