# You are given a complex . Your task is to convert it to polar coordinates.
# https://www.hackerrank.com/challenges/polar-coordinates/problem
from cmath import phase

z = input()

print(abs(complex(z)))
print(phase(complex(z)))
