n = int(input())
l = list(map(int,input().split()))
l=sorted(l)
if l[-1]==1:
    l[-1]=2
else:
    l[-1]=1
l=sorted(l)
print(*l)