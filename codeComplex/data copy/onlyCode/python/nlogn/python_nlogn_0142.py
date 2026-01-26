k = int(input().split()[1])
l = sorted(map(int, input().split()))

res = set()
for i in l:
    if i%k!=0:
        res.add(i)
    elif i//k not in res:
        res.add(i)
print(len(res))