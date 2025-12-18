n=input()
ans=0
r,c=0,0
for i in range(len(n)):
    r+=int(n[i])
    c+=1
    if int(n[i])%3==0 or r%3==0 or c==3:
        ans+=1
        r,c=0,0
print(ans)