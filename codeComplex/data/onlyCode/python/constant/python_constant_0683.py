import math

n, r = map(float, input().split())
a = math.pi / n
s = math.sin(a)
R = (r * s) / (1 - s)
print(R)
