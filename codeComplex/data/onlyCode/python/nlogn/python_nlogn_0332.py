n=int(input())
l=[]
nn=n
while n :
    n-=1
    s=input()
    l.append([len(s),s])
l.sort()
ch=1
i=1
#print(l[i][1])
ans=[]
for i in range(nn-1):
    if l[i][1] not in l[i+1][1]:
        ch=0
        break
    else:
    
        ans.append(l[i][1])
        
    
if ch:
    ans.append(l[nn-1][1])
    print("YES")
    
    print(*ans, sep = "\n")
else:
    print("NO")
        
        
