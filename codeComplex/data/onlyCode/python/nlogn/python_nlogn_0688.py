n,m=[int(x) for x in input().split()]
a=sorted([int(x) for x in input().split()])
b=[int(x) for x in input().split()]
if max(a)<min(b):
    print(sum(a)*m+sum(b)-a[-1]*(m-1)-a[-2])
elif max(a)==min(b):
    print(sum(a)*m+sum(b)-a[-1]*m)
else:
    print(-1)
    
