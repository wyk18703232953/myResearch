from collections import deque

n, m, k = map(int, input().split())
a = deque([int(i) for i in input().split()])

oper = 0
rem = 0
while a:
    x = a.popleft()
    pg = (x - 1 - rem) // k
    lrem = 1
    while a and (a[0] - 1 - rem) // k == pg:
        a.popleft()
        lrem += 1
    rem += lrem
    oper += 1
print(oper)
