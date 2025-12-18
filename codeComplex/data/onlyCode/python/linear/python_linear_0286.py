from sys import  stdin 
input=stdin.readline
from  collections import defaultdict
def num(s):
    l,r=0,0
    for i in s:
        if l==0 and i==")":
            r+=1
        elif i=="(":
            l+=1
        elif l and i==")":
            l-=1
    return (l,r)

def f(mp,cnt):
    ans=0
    # print(mp,cnt)
    for l in cnt:
        # print(mp,ans)
        if l.count(0)<1:
            continue
        if l!=(0,0) and l==l[::-1]:
            continue
        # print("l hai",l)
        t=mp[l[::-1]]
        t2=mp[l[::-1]]
        ans+=t
        if t and l!=l[::-1]:
            mp[l]-=1
    return ans

cnt=[]
mp=defaultdict(int)
for i in range(int(input())):
    s=input()
    l=num(s)
    # print(l,s)
    cnt.append(l)
    mp[l]+=1
print(f(mp,cnt))