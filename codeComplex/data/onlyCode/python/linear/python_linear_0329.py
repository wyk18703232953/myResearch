N,M=map(int,input().split())
L=[0]+[int(_) for _ in input().split()]+[M]
sumL=[0]
ans=-10**30
for i in range(1,N+1):
    sumL.append(sumL[-1]-(-1)**i*L[i])
for i in range(1,N+1):
    if L[i]>L[i-1]+1:
        ans=max(ans,2*sumL[i-1]-sumL[-1]-(-1)**(i)*(L[i]-1))
    if L[i]<L[i+1]-1:
        ans=max(ans,2*sumL[i]-sumL[-1]+(-1)**i*(L[i]+1))
if N%2==0:
    print(max(ans,sumL[-1]+M))
else:
    print(max(ans+M,sumL[-1]))