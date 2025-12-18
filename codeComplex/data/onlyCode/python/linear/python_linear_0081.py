a = list(input())
a = [int(x) for x in a]

b = list(input())
b = [int(x) for x in b]

n = len(a)
m = len(b)

ans = 0
for i in range(n):
    ans+=a[i]^b[i]
ones = [0 for i in range(m)]
zeros = [0 for i in range(m)]
# print(b)
for i in range(m):
    if b[i]:
        ones[i]=1
    else:
        zeros[i]=1
# print(ones,zeros)
for i in range(1,m):
    ones[i]+=ones[i-1]
    zeros[i]+=zeros[i-1]
    
for i in range(n):
    if a[i]==1:
        ans+=zeros[m-n+i]-zeros[i]
    else:
        ans+=ones[m-n+i]-ones[i]
print(ans)
