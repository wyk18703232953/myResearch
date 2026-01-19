hell=1000000007
id1=0
id2=0
a = []
def check(n,m,x):
    global id1,id2
    b = [0]*(1<<m)
    idx = [0]*(1<<m)
    for i in range(n):
        mask=0
        for j in range(m):
            if a[i][j]>=x:
                mask=mask^(1<<j)
        b[mask]=1
        idx[mask]=i+1
    for i in range(1<<m):
        if b[i]:
            for j in range(1<<m):
                if b[j]:
                    mask=i|j
                    if mask==((1<<m)-1):
                        id1=idx[i]
                        id2=idx[j]
                        return 1                        
    return 0
def meowmeow321():
    n,m = map(int,input().split())
    for i in range(n):
        dog = [int(x) for x in input().split()]
        a.append(dog)
    lo=0
    hi=hell
    while hi-lo>0:
        mid=(hi+lo+1)//2
        if check(n,m,mid):
            lo=mid
        else:
            hi=mid-1
    check(n,m,lo)
    print(id1,id2)
    
t=1
#t=int(input())
for xxx in range(t):
    meowmeow321()