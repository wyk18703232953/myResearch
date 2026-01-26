n,m = map(int,input().split())
d = {x:0 for x in range(m)}
l = []
for _ in range(n):
    s = input()
    for x in range(m):
        if s[x]== '1': d[x]+=1
    l.append(s)
for x in l:
    t=0
    for y in range(m):
        if x[y] =='1':
            if d[y] ==1:t = 1;break
    if t==0: print('YES');exit()
print('NO')