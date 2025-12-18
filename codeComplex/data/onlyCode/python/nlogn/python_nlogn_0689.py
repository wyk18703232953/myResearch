n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1.sort()
l2.sort()
l2=l2[::-1]
if n==1:
    if l1[0]!=min(l2):
        print(-1)
    else :
        print(sum(l2))
elif max(l1)>min(l2):
    print(-1)
else :
    ans=0
    l1=l1[::-1]
    if min(l2)==l1[0]:
        print(sum(l2) + (sum(l1)-l1[0])*m)
    elif min(l2)!=l1[0]:
        print(sum(l2)+l1[0]+sum(l1[1:])*m-l1[1])
                
            
        