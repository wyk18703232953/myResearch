def solve(a, b, c):
    D = b * b - 4 * a * c
    k = D**0.5
    x1 = (-b+k)/(2*a)
    x2 = (-b-k)/(2*a)
    return max(x1,x2)

from math import *
n, r = map(int, input().split())
a = (1/tan(pi/n))**2
b = -2 * r
c = -(r*r)
ans = solve(a,b,c)
print("%.10f" % ans)