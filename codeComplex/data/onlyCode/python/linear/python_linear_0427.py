n=int(input())
a=[]
for i in range(n):
    l=[int(i) for i in input().split()]
    if i==0:
        t=sum(l)
    a.append(sum(l))
a.sort(reverse=True)
print(a.index(t)+1)