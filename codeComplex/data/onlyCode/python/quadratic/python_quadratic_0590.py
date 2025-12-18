import sys
sss='RGB'*700
def check(ss,p):
    i=0
    m=10**5
    ans=0
    while i<len(p):
        if p[i]!=sss[i]:
            ans+=1
        i+=1
    m=min(m,ans)
    ans=0
    i=1
    while i<len(p)+1:
        if p[i-1]!=sss[i]:
            ans+=1
        i+=1
    m=min(m,ans)
    ans=0
    i=2
    while i<len(p)+2:
        if p[i-2]!=sss[i]:
            ans+=1
        i+=1
    m=min(m,ans)
    
    return m
    
        
for _ in range(int(input())):
    n,k=(list(map(int,sys.stdin.readline().split())))
    s=input()
    m=10**5
    for i in range(n-k+1):
        m=min(m,(check(sss,s[i:i+k])))
    print(m)    