# 1. Strings and Numbers
# 1.1. Write a console program that asks user for name, surname and age. After
# input
# is provided, program prints two different outputs sequentially:
# Name: <name>
# Surname: <surname>
# Age: <age>
# Person <name> <surname> is <age> years old.


print('Please enter Name, Surname and Age: ')
name = input('Name: ')
surname = input('Surname: ')
age = int(input('Age: '))

print('Person {0} {1} is {2} years old.'.format(name, surname, age))
print('Person {} {} is {} years old.'.format(name, surname, age))
