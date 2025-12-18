#!/bin/python2

from sys import stdin, stdout


N = 55

f = [0]
for i in range(1, N):
    f.append(f[-1]*4 + 1)
    if f[-1] > 1e18:
        break

t = int(stdin.readline().strip().split()[0])

for ca in range(0, t):
    n, m = [int(x) for x in stdin.readline().strip().split()]
    if n > 31:
        stdout.write("YES {}\n".format(n-1))
    else:
        # n <= 31
        start = 0
        found = False
        res = -1
        for i in range(1, n+1):
            start += 2**i -1
            end = start
            for k in range(1, i+1):
                end += f[n-k] * (2**(k+1) - 3)
            if m >= start and m <= end:
                found = True
                res = i
                break
        if found:
            stdout.write("YES {}\n".format(n-res))
        else:
            stdout.write("NO\n")

