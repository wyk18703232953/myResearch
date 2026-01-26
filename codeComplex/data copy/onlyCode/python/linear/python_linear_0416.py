n,k=map(int,input().split())
l=input()
l=sorted(l)
ans=l[0]
sum=ord(l[0])
index=0
for j in range(1,n):
    if len(ans)<k:
        if ord(l[j])-ord(l[index])>1:
            ans=ans+l[j]
            sum=sum+ord(l[j])
            index=j
    else:
        break
if len(ans)==k:
    sum=sum-96*k
    print(sum)
else:
    print(-1)        
        







    


             



