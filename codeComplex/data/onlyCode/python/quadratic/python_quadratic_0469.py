n = input()
l = map(int, raw_input().split())
r = map(int, raw_input().split())



mp = {i:i for i in range(n)}
out = [-1]*n
v = 0

a = n
done = set()
while v < n:
    ids = set()
    for j in range(n):
        if l[j] == r[j] == 0 and j not in done:
            ids.add(j)
            done.add(j)
    if len(ids) == 0:
        print('NO')
        exit()
    v += len(ids)
    for i in ids:
        out[mp[i]] = a
        for j in range(len(l)):
            if j < i:
                r[j] -= 1
            else:
                l[j] -= 1
    a -= 1
print('YES')
print(' '.join(map(str, out)))
