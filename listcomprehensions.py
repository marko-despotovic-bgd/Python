# You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n.
# Print a list of all possible coordinates given by  (i, j, k) on a 3D grid
# where the sum of  i + j + k is not equal to n.
# Here, 0<=i<=x;0<=j<=y;0<=k<=z;.
# Please use list comprehensions rather than multiple loops, as a learning exercise.


x, y, z, n = (int(input()) for _ in range(4))
print([[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a + b + c != n])