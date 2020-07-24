# 1. Strings and Numbers
# 1.2. Write a console program that asks for two numbers and prints their sum,
# difference, product and quotient.

print('Please enter two numbers: ')
a, b = (int(input()) for _ in range(2))
print('Sum: {}\nDifference: {}\nProduct: {}\nIntQuotient: {}\nFloatQuotient: {}'
      .format(a + b, a - b, a * b, a // b, a / b))
