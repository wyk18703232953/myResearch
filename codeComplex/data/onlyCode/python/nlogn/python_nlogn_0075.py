n,k=map(int,input().split())
l=[]
for i in range(n):
   manan,surbhi=map(int,input().split())
   l.append((manan,surbhi))

l.sort(key=lambda x:(x[0], -x[1]),reverse=True)
ans=1
ps=l[k-1][0]
tp=l[k-1][1]
for i in range(k,n):
    if l[i][0]==ps and l[i][1]==tp:
        ans+=1
    else:
        break
for i in range(k-2,-1,-1):
    if l[i][0]==ps and l[i][1]==tp:
        ans+=1
    else:
        break
             
print(ans)
