n, m = map(int, input().split())

l=[]
s1 = s2 = 0
for i in range(n):
    a, b = map(int, input().split())
    s1+=a
    s2+=b
    l.append(a-b)

if s1<=m: print(0)
elif s2>m: print(-1)
else:
    r=0
    l.sort(reverse=True)
    for i in l:
        r+=1
        s1-=i
        if s1<=m:
            print(r)
            break