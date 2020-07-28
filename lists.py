# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands
# where each command will be of the  types listed above.
# Iterate through each command in order and perform the corresponding
# operation on your list.


the_list = []

for _ in range(int(input())):
    line = input().split()
    print(line)
    if line[0] == 'print':
        print(the_list)
    if line[0] == 'append':
        the_list.append(int(line[1]))
    if line[0] == 'insert':
        the_list.insert(int(line[1]), int(line[2]))
        print(the_list)
    if line[0] == 'remove':
        # del the_list[int(line[1])]
        the_list.remove(int(line[1]))
        print(the_list)
    if line[0] == 'sort':
        the_list.sort()
        print(the_list)
    if line[0] == 'pop':
        the_list.pop()
        print(the_list)
    if line[0] == 'reverse':
        the_list.reverse()
        print(the_list)

