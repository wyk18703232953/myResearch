a , b = list(map(int, input().split()))
x, y, z = list(map(int, input().split()))
ans = 0
p = a - ((x*2) + y)
q = b - ((z*3) + y)
# print(p, q)
if (p < 0 and q < 0):
    print(abs(p) + abs(q))
elif (p < 0):
    print(abs(p))
elif (q < 0):
    print(abs(q))
else:
    print(0)