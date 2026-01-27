l,r=input().split(" ")
l,r=int(l),int(r)
if (l % 2 != 0):
    l+=1
if (l + 2 > r):
    print(-1);
else:
    print(l,l+1,l+2)
            
                
                
