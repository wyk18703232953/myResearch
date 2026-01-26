n, k = map(int, input().split())

a = 1
b = -(2*n+3)
c = (n*n+n-2*k)

d = int((b*b - 4*a*c) ** 0.5)

s1 = (-b + d) // (2 * a)
s2 = (-b - d) // (2 * a)
if s1 >= 0 and s1 <= n:
    print(s1)
else:
    print(s2)
