l = list(map(int,input().split()))
n = 0
m=-1
while(n<14):
    c=0
    g = l.copy()
    div = l[n]//14
    h = l[n]%14
    i = n+1
    sum = div*14
    g[n]=0
    while(sum):
        if i==14:
            i=0
        g[i]+=div
        sum-=div
        i+=1
    i = n+1
    while(h):
        if i==14:
            i=0
        g[i]+=1
        h-=1
        i+=1
    for j in g:
        if j%2==0:
            c+=j

    m = max(c,m)
    n+=1
print(m)

