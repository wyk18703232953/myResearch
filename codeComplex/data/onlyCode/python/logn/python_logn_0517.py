from math import floor
from sys import stdin

CONST = 9

def solve(k):
    i = 0
    while k > CONST * (10 ** i) * (i + 1):
        k -= floor(CONST * (10 ** i)) * (i + 1)
        i += 1
    num_digits = i + 1
    num = floor((k - 1) / num_digits)
    num += floor(10 ** (i))
    print(('{}'.format(num))[(k - 1) % num_digits])

if __name__ == '__main__':
    for line in stdin:
        solve(int(line.rstrip()))