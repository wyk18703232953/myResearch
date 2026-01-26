n,pos,l,r = map(int,input().split())
if(r-l+1 == n):
    print(0)
    exit(0)
if(pos>l and pos<r):
    if(n>r and l>1):
        x = pos-l+1+r-l+1
        y = r-pos+1+r-l+1
        ans = min(x,y)
    else:
        if(n==r):
            ans = pos-l+1
        elif(l==1):
            ans = r-pos+1
elif(pos>=r):
    if(n>r):
        ans = pos-r+1
    else:
        ans = 0
    if(l>1):
        ans+=r-l+1
elif(pos<=l):
    if(l>1):
        ans = l-pos+1
    else:
        ans = 0
    if(n>r):
        ans+=r-l+1
print(ans)
    