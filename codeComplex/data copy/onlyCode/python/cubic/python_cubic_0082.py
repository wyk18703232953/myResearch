import sys
from array import array  # noqa: F401
from itertools import product
from collections import deque


def input():
    with open('input.txt') as fp:
        return fp.readlines()


def output(ans: str):
    with open('output.txt', mode='w') as fp:
        fp.write(ans)


'''
def input():
    return [line.decode('utf-8') for line in sys.stdin.buffer.readlines()]


def output(ans):
    print(ans)
'''


s = input()
n, m = map(int, s[0].split())
k = int(s[1])
a = [[0] * m for _ in range(n)]
dq = deque()
line = list(map(lambda x: int(x) - 1, s[2].split()))
for i in range(0, 2 * k, 2):
    a[line[i]][line[i + 1]] = 1
    dq.append((line[i], line[i + 1]))


x, y = -1, -1
while dq:
    x, y = dq.popleft()
    for tx, ty in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if 0 <= tx < n and 0 <= ty < m and not a[tx][ty]:
            a[tx][ty] = 1
            dq.append((tx, ty))

output(f'{x+1} {y+1}')
