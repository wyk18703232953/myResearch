a=int(input())
z=list(map(int,input().split()))
ans=[]
k=len(z)
for i in range(len(z)):
    if((z[i]-i)%len(z)==0):
        ans.append((z[i]-i)//k)
    else:
        ans.append((z[i]-i)//k)
        ans[-1]+=1
t=min(ans)
print(ans.index(t)+1)
