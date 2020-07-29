# 1. Strings and Numbers
# 1.1 Write a console program that asks user for name, surname and age. After
# input
# is provided, program prints two different outputs sequentially:
# Name: <name>
# Surname: <surname>
# Age: <age>
# Person <name> <surname> is <age> years old.
# 2. Conditionals
# 2.3. Add authentication capability.
# The program should first ask a user to register by sequentially asking for
# user's name, surname, age, username and password.
# Then it should offer user to login.
# When user tries to log in, program asks for username and password.
# If provided username and password are correct, program prints user's
# information (name, surname etc.);
# otherwise error message is printed. Once logged in, user should be able to
# log out.


print('Please fill registration form. Enter Name, Surname and Age: ')
name, surname = (input('Name: '), input('Surname: '))
age = int(input('Age: '))

while True:
    print('Please login using valid credentials: ')
    login_name, login_surname = (input('Name: '), input('Surname: '))
    if login_name != name or login_surname != surname:
        print('You have entered invalid username or password!')
    else:
        print('Person {0} {1} is {2} years old.'.format(name, surname, age))
        print('Person {} {} is {} years old.'.format(name, surname, age))
        logout = input('Type credentials again or \'logout\' for logout')
        if logout.lower() == 'logout':
            break
