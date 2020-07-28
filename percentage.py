# The first line contains the integer n, the number of students' records.
# The next  lines contain the names and marks obtained by a student, each value separated by a space.
# The final line contains query_name, the name of a student to query.


marks = {}
for _ in range(int(input())):
    line = input().split()
    marks[line[0]] = list(map(float, line[1:]))
print('{}'.format(sum(marks[input()])/3))
