n, m=[int(k) for k in input().split()]
w=[int(k) for k in input().split()]
w=[0]+w+[m]
c, d=[], []
res=0
for j in range(n+1):
    c.append(res)
    if j%2==0:
        res+=w[j+1]-w[j]
res=0
for j in range(n+1, -1, -1):
    if j%2==0 and j!=n+1:
        res+=w[j+1]-w[j]
    d.append(res)
d=d[::-1]
mx=d[0]
for j in range(n+1):
    mx=max(c[j]+(w[j+1]-w[j]-1)+(m-w[j+1]-d[j+1]), mx)
#print(c)
#print(d)
print(mx)