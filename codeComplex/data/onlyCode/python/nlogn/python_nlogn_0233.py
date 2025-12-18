from math import gcd
import sys

#Library Info(ACL for Python/Pypy) -> https://github.com/not522/ac-library-python


def input():
    return sys.stdin.readline().rstrip()


DXY = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # L,D,R,Uの順番

def on_one_line(Points):
    n = len(Points)
    s = set([])
    for i in range(1,n):
        x,y = Points[i][0] - Points[0][0],Points[i][1] - Points[0][1]
        g = gcd(x,y)
        x //= g
        y //= g 
        if (x < 0):
            x *= -1;y *= -1
        if (x == 0):
            y = abs(y)
        s.add((x,y))
    return len(s) == 1

def main():
    n = int(input())
    Ps = [tuple(map(int, input().split())) for i in range(n)]
    if n <= 2:
        print("YES")
        return 0
    if on_one_line(Ps):
        print("YES")
        return 0

    p,q = Ps[1][0] - Ps[0][0],Ps[1][1] - Ps[0][1]
    g = gcd(p,q)
    p //= g;q //= g
    if (p < 0):p *= -1;q *= -1
    elif (p == 0):q = abs(q)

    not_same = []
    for i in range(2,n):
        x,y = Ps[i][0] - Ps[0][0],Ps[i][1] - Ps[0][1]
        x,y = x//gcd(x,y),y//gcd(x,y)
        if (x < 0):x *= -1;y *= -1
        if (x == 0):y = abs(y)
        if (x,y) != (p,q):
            not_same.append(Ps[i])

    if len(not_same) <= 1:
        print("YES")
        return 0
    
    if on_one_line(not_same):
        print("YES")
        return 0
    
    p,q = not_same[0][0] - Ps[0][0],not_same[0][1] - Ps[0][1]
    P,Q = not_same[0]
    g = gcd(p,q)
    p //= g;q //= g
    if (p < 0):p *= -1;q *= -1
    elif (p == 0):q = abs(q) 
    not_same = []

    for i in range(n):
        x,y = Ps[i][0] - Ps[0][0],Ps[i][1] - Ps[0][1]
        if (x == 0 and y == 0):continue
        x,y = x//gcd(x,y),y//gcd(x,y)
        if (x < 0):x *= -1;y *= -1
        if (x == 0):y = abs(y)
        if (x,y) != (p,q):
            not_same.append(Ps[i])

    if len(not_same) <= 1:
        print("YES")
        return 0
    
    if on_one_line(not_same):
        print("YES")
        return 0  
    
    p,q = P - Ps[1][0],Q - Ps[1][1]
    g = gcd(p,q)
    p //= g;q //= g
    if (p < 0):p *= -1;q *= -1
    elif (p == 0):q = abs(q) 

    not_same = []
    for i in range(n):
        x,y = Ps[i][0] - Ps[1][0],Ps[i][1] - Ps[1][1]
        if (x == 0 and y == 0):continue
        x,y = x//gcd(x,y),y//gcd(x,y)
        if (x < 0):x *= -1;y *= -1
        if (x == 0):y = abs(y)
        if (x,y) != (p,q):
            not_same.append(Ps[i])

    if len(not_same) <= 1:
        print("YES")
        return 0
    
    if on_one_line(not_same):
        print("YES")
        return 0  

    print("NO")
    return 0


if __name__ == "__main__":
    main()

