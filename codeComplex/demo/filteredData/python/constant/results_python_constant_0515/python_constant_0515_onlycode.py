from sys import stdin, stdout
from math import sin, tan, cos

x, y, z, t1, t2, t3 = map(int, stdin.readline().split())

if abs(x - z) * t2 + abs(x - y) * t2 + 3 * t3 <= abs(x - y) * t1:
    stdout.write('YES')
else:
    stdout.write('NO')