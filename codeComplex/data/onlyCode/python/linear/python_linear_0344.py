n,d=[int(x) for x in input().split(" ")]
a=[int(x) for x in input().split(" ")]
pos=2
for i in range(n-1):
    l=a[i]+d
    r=a[i+1]-d
    if l==r:
        pos+=1
    elif l<r:
        pos+=2
print(pos)
