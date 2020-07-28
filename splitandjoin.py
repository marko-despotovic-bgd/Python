# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.


line = input()
line = line.split(" ")
print(line)
line = "-".join(line)
print(line)
