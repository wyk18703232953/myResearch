import math
n,pos,l,r = map(int, input().strip().split(' '))
#n=int(input())
#lst = list(map(str, input().strip().split(' ')))
if l==1 and r==n:
    print(0)
elif l==1:
    if pos==r:
        print(1)
    elif pos>r:
        print(pos-r+1)
    elif pos<r:
        print(r-pos+1)
elif r==n:
    if pos==l:
        print(1)
    elif pos<l:
        print(l-pos+1)
    else:
        print(pos-l+1)
else:
    if pos>=l and pos<=r:
        if pos-l<r-pos:
            print(2+pos-l+r-l)
        else:
            print(2+r-l+r-pos)
    else:
        if pos>r:
            print(pos-r+2+r-l)
        else:
            print(l-pos+2+r-l)