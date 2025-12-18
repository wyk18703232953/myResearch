n,m=map(int,input().split())
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
for i in list1:
    if i in list2:
        print(i,end=' ')
