inf=10**9

n=int(input())
t=[0]*n
m={}
for j in range(n):


    s=input()


    bal=0
    req=0

    for i in s:
        if i==")":
            bal-=1
        else:
            if bal<0:
                req+=bal
                bal=1
            else:
                bal+=1

    if req<0:
        if bal>0:
            req=inf
        else:
            req+=bal
    else:
        req=bal

    t[j]=req

    if req not in m:
        m[req]=1
    else:
        m[req]+=1

res=0

for i in t:
    if i>=0:
        if -i in m:
            res+=m[-i]

print(res)
