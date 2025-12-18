import sys
if locals()['__file__'][-2:] == 'py':
    sys.stdin = open('in.txt', 'r')
n = int(input())
a = []
for i in range(1, n + 1):
    l, r = map(int, input().split())
    a.append([l, -r, i])
a.sort()
ma = a[0][1]
nma = a[0][2]
for i in range(1, n):
    if a[i][1] >= ma:
        print(a[i][2], nma)
        exit()
    else:
        ma = a[i][1]
        nma = a[i][2]
print(-1, -1)
