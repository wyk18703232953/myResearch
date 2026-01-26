def if_spruce(n,l,s):
    d=[0]*(n+1)
    for i in range(1,n+1):
        if i not in s:
            d[l[i]]+=1
    for i in range(1,n+1):
        if i in s and d[i]<3:
            return "No"
    return "Yes"
 
n=int(input())
l,a=[0]*2,0
for _ in range(n-1):
    a=int(input())
    l.append(a)
s=set(l)
print(if_spruce(n,l,s))