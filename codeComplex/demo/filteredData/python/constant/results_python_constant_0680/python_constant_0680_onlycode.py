
import sys


def query(c, d):
    print('? %d %d' % (c, d))
    sys.stdout.flush()
    res = int(input())
    return res

a = 0
b = 0
big = query(0, 0)

for i in range(29, -1, -1):
    p = query(a ^ (1 << i), b)
    q = query(a, b ^ (1 << i))
    if p == q:
        if big == 1:
            a ^= 1 << i
        else:
            b ^= 1 << i
        big = p
    elif p == -1:
        a ^= 1 << i
        b ^= 1 << i

print('! %d %d' % (a, b))
sys.stdout.flush()
