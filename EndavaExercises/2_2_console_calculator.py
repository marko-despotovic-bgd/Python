# 2. Conditionals
# 1.2. Write a console program that asks for two numbers and prints their sum,
# difference, product and quotient.
# 2.2. Make a console calculator. Console program should
# ask user for two numbers and the operation the user wants to be executed
# (addition, subtraction, multiplication, division); then it provides a result.


while True:
    print('Please enter two numbers: ')
    a, b = (int(input()) for _ in range(2))
    operation = input('Please enter operation (S for sum, D for division, '
                      'P for product or Q for quotient: ')
    if operation.lower() == 's':
        print('Sum is: {}'.format(a + b))
    elif operation.lower() == 'd':
        print('Difference is: {}'.format(abs(a - b)))
    elif operation.lower() == 'p':
        print('Product is: {}'.format(a * b))
    elif operation.lower() == 'q':
        print('IntQuotient is: {}\nFloatQuotient is: {}'.format(a // b, a / b))
    else:
        exit()

