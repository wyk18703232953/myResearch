s=input()
ans=0
m=set()
for i in range(len(s)):
    for j in range(i,-1,-1):
        if(s[j:i+1] in m):
            ans=max(ans,i-j+1)
        else:
            m.add(s[j:i+1])
print(ans)
    