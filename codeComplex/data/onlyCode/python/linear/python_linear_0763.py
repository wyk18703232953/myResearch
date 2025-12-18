def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))

from collections import deque

n, m = getList()
nums = getList()
mxnum = max(nums)
d = deque(nums)

qr = []
for i in range(m):
    qr.append(getN())

log = []

rot = 0
while(True):
    # print(d)
    a = d.popleft()
    b = d.popleft()
    log.append((a, b))
    if a > b:
        a, b = b, a

    d.append(a)
    d.appendleft(b)

    rot += 1

    if b == mxnum:
        break



for q in qr:
    if q <= rot:
        print(log[q - 1][0], log[q - 1][1])
    else:
        res = q -  rot - 1
        print(b, d[res % (n-1) + 1  ])

# print(d)
"""
5 10
1 2 5 4 3
1
2
3
4
5
6
7
8
9
10
"""
