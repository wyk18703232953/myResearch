n=input()
ans=0
r,c=0,0
for i in n:
    r+=int(i)
    c+=1
    if int(i)%3==0 or r%3==0 or c==3:
        ans+=1
        r,c=0,0
print(ans)