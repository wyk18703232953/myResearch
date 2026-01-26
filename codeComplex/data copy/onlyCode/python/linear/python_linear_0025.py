n=int(input())
li=list(map(int,input().split()))
lis=[x%2 for x in li]
if lis.count(0)>lis.count(1):
    print(lis.index(1)+1)
else:
    print(lis.index(0)+1)