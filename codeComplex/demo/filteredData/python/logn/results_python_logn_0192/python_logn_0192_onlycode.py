def bin(num):
    i=9*num*11
    count=0
    add=0
    for j in range(100):
        add=0
        a=str(i)
        for k in range(10):
            add+=(a.count(str(k))*k)
        if i-add>=s:
            return i
        i+=1
    return -1


n,s=map(int,input().split())
i=0
j=10**30
limit=0
while i<j:
    m=(i+j)//2
    if bin(m) == -1:
        i=m+1
    else:
        j=m
print(max(0,n-bin(i)+1))