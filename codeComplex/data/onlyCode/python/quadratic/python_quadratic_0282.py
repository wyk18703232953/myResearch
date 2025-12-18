n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
# set1=set(l1)
# set2=set(l2)
# final=set1.intersection(set2)

for i in l1:
    if i in l2:
        print(i,end=" ")
    