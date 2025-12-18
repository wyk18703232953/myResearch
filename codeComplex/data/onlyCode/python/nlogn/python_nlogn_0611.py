from bisect import bisect_right,bisect_left
n,c_tv,c_es=map(int,input().split())
start=[]
end=[]
add=0
for _ in range(n):
    l,r=map(int,input().split())
    add+=(r-l)
    start.append(l)
    end.append(r)
start.sort()
end.sort()
ans=add*c_es+n*c_tv
M=10**9+7
v=[0]*(n+1)
for i in range(n):
    indx=bisect_left(end,start[i])-1
    k=indx
    while k>=0 and (start[i]-end[k])*c_es<c_tv and v[k]==1:
        k-=1
    if k==-1:
        continue
    if (start[i]-end[k])*c_es<c_tv:
        ans-=c_tv-(start[i]-end[k])*c_es
        v[k]=1
print(ans%M)