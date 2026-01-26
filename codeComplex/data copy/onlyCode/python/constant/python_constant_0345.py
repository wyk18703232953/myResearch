from sys import stdin
n = int(stdin.readline()) + 1
if n == 1:
    print(0)
else:
    print(n//2 if n%2 == 0 else n)