# 3. Iterations and Collections
# Modify program from (2.3): add support for multiple users.
# 2.3. Add authentication capability.
# The program should first ask a user to register by sequentially asking for
# user's name, surname, age, username and password.
# Then it should offer user to login.
# When user tries to log in, program asks for username and password.
# If provided username and password are correct, program prints user's
# information (name, surname etc.);
# otherwise error message is printed. Once logged in, user should be able to
# log out.
# 3.2. Once program is started it in state (A); it expects one of following commands: "register" or "login".
# "register" command initiates register flow, after which program again enters state (A).
# User then can register another user, or try to login, etc.
# If user enters command "login" program asks user for username and password,
# authenticates user against already registered users, and prints his data.
# User stays logged in until user enters command "logout". Then program is again in state (A).


person_list = []
person = []
while True:
    reg_or_login = input('Do you want to register or login?\n'
                         'For registration, enter \'register\'.\n'
                         'For login, enter \'login\': ')

    if reg_or_login.lower() == 'register':
        name, surname, age = input('Input name: '), input('Input surname: '), input('Input age: ')
        person = [name, surname, age]
        print(person)
        person_list.append(person)
        print(person_list)

    elif reg_or_login.lower() == 'login':
        while True:
            print('Please login using valid credentials: ')
            login_name, login_surname = (input('Name: '), input('Surname: '))
            print(person_list)
            for person in person_list:
                if person.__contains__(login_name) and person.__contains__(login_surname):
                    while True:
                        logout = input('You have successfully logged in!\nType \'logout\' for logout! ')
                        if logout.lower() != 'logout':
                            print('You entered: {}'.format(logout))
                        else:
                            break
                    break
            else:
                print('You have entered invalid username or password!')

    else:
        print('You did not entered correct option!')
        break
