import sys,math
a,b=map(int,input().split())
l=list(map(int,input().split()))
t=[[-1,0] for i in range(100001)]
for i in range(a):
    if t[l[i]][0]!=-1:print(0);sys.exit()
    t[l[i]][0]=3
s=math.inf
for i in range(a):
    if t[l[i]&b][0]!=-1:
        #print(l[i],t[l[i]&b])
        if l[i]&b!=l[i] and t[l[i]&b][0]!=1:
            t[l[i]&b]=[1,min(2,t[l[i]&b][1]+1)]
        #print(l[i],t[l[i]&b])
    else:t[l[i]&b]=[2,1]
#for i in range(11):print(t[i])
for i in range(a):
    if t[l[i]&b][1]!=0 and t[l[i]&b][0]==1:s=min(s,t[l[i]&b][1])
if s==math.inf:
    print(-1)
else:
    print(s)
