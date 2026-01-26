n=int(input())
l1=list(map(int,input().split()))
if len(list(set(l1)))==1 and l1[0]>0:
    print(1)
else:
    l2=list(set(l1))
    x=l1.count(0)
    if x==0:
        print(len(l2))
    else:
        print(len(l2)-1)
    