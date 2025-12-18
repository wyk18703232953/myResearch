import bisect
def solve(l,d,s2,r):
    ans=""
    lol=0
    i=0
    lo=0
    while i<(len(s2)):
        if(lo==1):
            #print("lol",i)
            
            a=s2[i]
            ind=bisect.bisect_left(l,a)
            #print(ind,a)
            for x in range(ind,-1,-1):
                if(l[x]<l[ind]):
                    ind=x
                    #print("lol")
                    break
            ans+=str(l[ind])
            d[l.pop(ind)]-=1
            
            lol=1
            break

        a=s2[i]
        ind=bisect.bisect_left(l,a)
        #print(l,ind,a)
        
        if(ind==len(l)):
            ind-=1
            ans+=str(l[ind])
            d[l[ind]]-=1
            lol=1
            break
        elif(l[ind]>a):
            if(ind==0):
                while ind==0:
                    
                    l.append(int(ans[-1]))
                    d[int(ans[-1])]+=1
                    l.sort()
                    ans=ans[:len(ans)-1]
                    lo=1
                    i-=1
                    a=s2[i]
                    ind=bisect.bisect_left(l,a)
                #print(i)
                #i+=1
                continue
            lol=1
            ans+=str(l[ind-1])
            #print(ans,i)
            d[l[ind-1]]-=1
            l.pop(ind-1)
            break
        else:
            ans+=str(l[ind])
            d[l[ind]]-=1
            l.pop(ind)
        i+=1
    ll=[]
    #print("lol",d)
    if(lol):
        for i in d:
            if(d[i]!=0):
                ll.append(i)
        ll.sort(reverse=True)
        co=0
        #print(ll)
        for i in ll:
            for j in range(d[i]):
                if(i==0):
                    co+=1
                    if(co>r):
                        break
                ans+=str(i)
                
    print(ans)
from math import gcd
import sys
from collections import defaultdict as dd
input=sys.stdin.readline
s1=list(map(int,input().strip()))
s2=list(map(int,input().strip()))
z=s1.count(0)
d=dd(int)
n=len(s1)
m=len(s2)
l=sorted(s1)
for i in s1:
    d[i]+=1
if len(s1)<len(s2):
    for i in range(len(s1)-1,-1,-1):
        print(l[i],end="")
elif(len(s1)>len(s2)):
    r=m-(n-z)
    #print(l,m,n,z)
    l=l[z-r:]
    #print(l,r)
    solve(l,d,s2,r)
else:
    solve(l,d,s2,100)
    