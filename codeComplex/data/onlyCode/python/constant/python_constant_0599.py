from __future__ import division
from sys import stdin, stdout
from math import ceil

def write(x):
    stdout.write(str(x) + "\n")


n, k = map(int, stdin.readline().split())

red = 2 * n

green = 5 * n

blue = 8 * n


need = int(ceil(red / k)) + int(ceil(green / k)) + int(ceil(blue / k))

write(need)
