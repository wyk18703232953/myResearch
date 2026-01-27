from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a = round((n / 2) ** 0.5)
    b = round((n / 4) ** 0.5)
    if 2*a**2 == n or 4*b**2 == n:
        print("YES")
    else:
        print("NO")
