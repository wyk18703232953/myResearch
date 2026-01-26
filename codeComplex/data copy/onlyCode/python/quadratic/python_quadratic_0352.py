n=int(input())
s=list(input())
t=list(input())

cnt=0
ans=[]
f1=0
for i in range(n):
    if s[i]==t[i]:
        continue
    f=0
    for j in range(i+1,n):
        if s[j]==t[i]:
            f=1
            for k in range(j,i,-1):
                s[k-1],s[k]=s[k],s[k-1]
                ans.append(k)
            break
    if f==0:
        print(-1)
        exit()

print(len(ans))
print(*ans)