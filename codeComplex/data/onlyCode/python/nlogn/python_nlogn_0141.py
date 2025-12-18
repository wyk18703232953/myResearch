k = int(input().split()[1])
l = sorted(list(map(int,input().split())))

res = set()
for i in l:
    if i//k  not in res or i%k!=0:
        res.add(i)

print(len(res))