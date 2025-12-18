from __future__ import division
from sys import stdin, stdout


def write(x):
    stdout.write(str(x) + "\n")


n, s = map(int, stdin.readline().split())

if s % n == 0:
    write(s // n)
else:
    write(s // n + 1)
