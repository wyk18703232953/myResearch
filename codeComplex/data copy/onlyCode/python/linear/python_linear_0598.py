from __future__ import division
from sys import stdin, stdout


def write(x):
    stdout.write(str(x) + "\n")


n = int(stdin.readline())
out = 0
for i in range(2, n + 1):
    out += 4 * (n // i - 1) * i

write(out)
