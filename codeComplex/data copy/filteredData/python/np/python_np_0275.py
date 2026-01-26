import math
import queue
import sys

MOD = 10**9 + 7
sys.setrecursionlimit(1000000)

def hgt(x, N):
    if x == 0:
        return -1
    h = 0
    while x & 1 != 1:
        h += 1
        x = x >> 1
    return h

def up(x, N):
    h = hgt(x, N)
    g = x + (1 << h)
    if g > 0 and g < N and hgt(g, N) == h + 1:
        return g
    g = x - (1 << h)
    if g > 0 and g < N and hgt(g, N) == h + 1:
        return g
    return x

def left(x, N):
    h = hgt(x, N)
    if h == 0:
        return x
    g = x - (1 << (h - 1))
    if g > 0:
        return g
    return x

def right(x, N):
    h = hgt(x, N)
    if h == 0:
        return x
    g = x + (1 << (h - 1))
    if g < N:
        return g
    return x

def main(n):
    if n <= 0:
        return
    N = n + 1
    q = n
    for i in range(1, q + 1):
        p = (i % (N - 1)) + 1 if N > 1 else 1
        length = 1 + (i % max(1, (n.bit_length() + 1)))
        dirs = []
        for j in range(length):
            r = (i + j) % 3
            if r == 0:
                dirs.append('U')
            elif r == 1:
                dirs.append('L')
            else:
                dirs.append('R')
        for c in dirs:
            if c == 'U':
                p = up(p, N)
            elif c == 'R':
                p = right(p, N)
            else:
                p = left(p, N)
        print(p)

if __name__ == "__main__":
    main(10)