import sys

n, q = map(int, input().split())
top = len(bin(n >> 1)) - 2
ans = [1] * q

for i in range(q):
    v = int(input())
    s = input()
    if n == 1:
        continue
    for h in range(top+1):
        if v & (1 << h):
            break

    for c in s:
        if h == top and c == 'U' or h == 0 and c != 'U':
            continue
        if c == 'U':
            v -= 1 << h
            h += 1
            v |= 1 << h
        elif c == 'L':
            v -= 1 << h
            h -= 1
            v |= 1 << h
        else:
            h -= 1
            v |= 1 << h
    ans[i] = v

print(*ans, sep='\n')
