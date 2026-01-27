from math import sqrt
for _ in ' '*int(input()):
    n = int(input())
    if int(sqrt(n/2)) == sqrt(n/2) or int(sqrt(n/4)) == sqrt(n/4):
        print("YES")
    else: print("NO")