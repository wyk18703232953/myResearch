
#FAILED
n = int(input())
l = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]

items = [(-l[i]-r[i],i) for i in range(n)]
items.sort()
vals = [1] * n
m = 1
for i in range(1, n):
    if items[i-1][0] != items[i][0]:
        m += 1
    vals[items[i][1]] = m

for i in range(n):
    ln = sum(map(lambda x: x-vals[i] > 0, vals[:i]))
    lr = sum(map(lambda x: x-vals[i] > 0, vals[i:]))
    if ln != l[i] or lr != r[i]:
        print('NO')
        break
else:
    print('YES')
    print(' '.join(str(i) for i in vals))
