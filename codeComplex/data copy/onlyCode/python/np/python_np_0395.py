import io,os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n,m=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]
l=-1;r=10**9+1
ans1,ans2=-1,-1
while r-l>1:
    x=(l+r)//2
    idx={}
    for i in range(n):
        v=0
        for j in range(m):
            if a[i][j]>=x:
                v+=1
            v<<=1
        idx[v>>1]=i
    ok=False
    idx1,idx2=0,0
    for aa,bb in idx.items():
        for cc,dd in idx.items():
            for d in range(m):
                if (aa|cc)==(2**m)-1:
                    ok=True
                    idx1=bb+1
                    idx2=dd+1
    if ok:
        l=x
        ans1=idx1
        ans2=idx2
    else:
        r=x
print(ans1,ans2)