n,l,r,x = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(1,(2**n)+1):
    j = bin(i)
    j = j[2:]
    if len(j)<n:
        j = '0'*(n-len(j))+j
    #print(j)
    c = 0
    temp = []
    for k in j:
        if k=='1':
            temp.append(a[c])
        c+=1
    s = sum(temp)
    #print(s)
    if len(temp)>=2 and s>=l and s<=r and (max(temp)-min(temp))>=x:
        ans+=1
    #print(ans)
    #print()
    #print(j)
print(ans)