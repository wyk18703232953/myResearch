n=int(input())
l=list(map(int,input().split()))
m=l[:]
m.sort()
f=1
c=0
for i in range(n):
    if(l[i]!=m[i]):
        c+=1 
    if(c>2):
        f=0 
        break 
if(f==0):
    print("NO")
else:
    print("YES")
    
        
            
        
