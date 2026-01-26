l,r=map(int,input().split())
a=bin(l)
b=bin(r)
a="0"*(len(b)-len(a))+a[2:len(a)]
b=b[2:len(b)]
c=[0 for i in range(len(a))]
flag=False
for i in range(len(a)):
    if(a[i]!=b[i]):
        flag=True
    if(flag):c[i]=1
ans=0    
for j in range(len(a)):
    ans+=c[len(a)-1-j]*(2**(j))
print(ans)    