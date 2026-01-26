import math

def solve(n) :
    if not n%2 and math.sqrt(n//2) == int(math.sqrt(n//2)) :
        print('YES')
        return
    if not n%4 and math.sqrt(n//4) == int(math.sqrt(n//4)) :
        print('YES')
        return
    print('NO')

t = int(input())
for i in range(t) :
    n = int(input())
    solve(n)