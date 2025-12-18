N,M=map(int,input().split())
light=[0]+[int(_) for _ in input().split()]+[M]
sumlist=[]
sumlight,ans=0,-10**30
for i in range(N+1):
    sumlight+=(-1)**(i+1)*light[i]
    sumlist.append(sumlight)
for i in range(1,N+1):
    if light[i]>light[i-1]+1:
        ans=max(ans,2*sumlist[i-1]-sumlight+(-1)**(i+1)*(light[i]-1))
    if light[i]<light[i+1]-1:
        ans=max(ans,2*sumlist[i]-sumlight+(-1)**i*(light[i]+1))
if N%2==0:
    print(max(ans,sumlight+M))
else:
    print(max(ans+M,sumlight))