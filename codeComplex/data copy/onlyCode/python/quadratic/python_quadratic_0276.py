n , m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in range(n):
    for j in range(m):
        if l1[i]==l2[j]:
            if l1[i] is not l3:
                l3.append(l1[i])
print(*l3)
                