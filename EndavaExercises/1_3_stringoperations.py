# 1. Strings and Numbers
# 1.3. Write a console program that asks for a string and outputs string length
# as well as first and last three characters.

print('Please enter some string: ')
string = (input())

print('Length: {}\nFirst 3 chars: {}\nLast 3 chars: {}'.format(len(string),
                                                               string[:3],
      string[-3::1]))
