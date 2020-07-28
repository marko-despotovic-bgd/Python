# Given an integer,n , and n space-separated integers as input, create a tuple,t , of those n integers.
# Then compute and print the result of hash(t).


n = int(input())
integer_list = map(int, input().split())
integer_list = [int(x) for x in integer_list]
print(integer_list)
t = tuple(integer_list)
print(hash(t))
