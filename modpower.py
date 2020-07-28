# You are given three integers: , , and , respectively. Print two lines.
# The first line should print the result of pow(a,b).
# The second line should print the result of pow(a,b,m).


a, b, m = (int(input()) for _ in range(3))
print(pow(a, b))
print(pow(a, b, m))