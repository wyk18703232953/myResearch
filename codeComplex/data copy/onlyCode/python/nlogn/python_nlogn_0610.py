from bisect import bisect_right
n, x, y = map(int, input().split(' '))
s=[0]*n
e=[0]*n
v=[0]*n
c=0
for i in range(n):
    s[i],e[i]=map(int, input().split(' '))
    c+=x+(e[i]-s[i])*y
s.sort()
e.sort()
for i in range(n-2,-1,-1):
    k=bisect_right(s,e[i])
    while (k < n)  and (v[k]==1) and (s[k]-e[i]) * y < x :
        k+=1
    if k==n:
        continue
    if (s[k]-e[i]) * y < x :
        v[k] = 1
        c+=(s[k]-e[i])*y-x
 
print(c%(10**9+7))