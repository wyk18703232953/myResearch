n, a, b = [int(i) for i in input().split()]
lst = sorted([int(i) for i in input().split()])
print(lst[b]-lst[b-1])
