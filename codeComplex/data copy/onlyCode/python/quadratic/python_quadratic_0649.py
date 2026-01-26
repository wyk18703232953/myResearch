n = int(input())
l = [int(i) for i in input().split()]
l.sort()
s = set([l[0]])
res = 1
for i in l:
    f = 1
    for j in s:
        if(i%j == 0):
            f = 0
            break
    if(f):
        s.add(i)
        res += 1
print(res)