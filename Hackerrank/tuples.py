n = int(input())
integer_list = map(int, input().split())
integer_list = [int(x) for x in integer_list]
print(integer_list)
t = tuple(integer_list)
print(hash(t))
