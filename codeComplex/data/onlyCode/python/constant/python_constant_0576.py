n = int(input())
x, y = map(int, input().split())
na = abs(x - 1) + abs(y - 1)
nb = abs(n - x) + abs(n - y)
if na <= nb:
    print("white")
else:
    print("black")
