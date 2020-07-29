# Write a console program which asks user for string input repeatedly until user inputs string "end".
# All string inputs are stored.
# Then program asks user to enter search phrase.
# Program then prints all strings which contain the search phrase.
# The program asks user again to enter another search phrase.
# Program terminates when user enters search phrase "exit".


list_of_strings = []
while True:
    items = input('Enter list item or type \'end''\' when done: ')
    if items != 'end':
        list_of_strings.append(items)
    else:
        break

print(list_of_strings)

while True:
    phrase = input('Enter search phrase or \'exit\' to terminate program: ')
    if phrase != 'exit':
        search_list = []
        for i in list_of_strings:
            if i.__contains__(phrase):
                search_list.append(i)
        print(search_list)
    else:
        break


