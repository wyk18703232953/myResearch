import sys
input=sys.stdin.readline
n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append([int(i) for i in input().split()])
left=0
right=10**9+1
while left<right:
    mid=(left+right)//2
    dicta={}
    for i in range(n):
        mask=0
        for j in range(m):
            mask<<=1
            if l[i][j]>=mid:
                mask+=1
        dicta[mask]=i
    ok=False
    for i in dicta:
        for j in dicta:
            if i|j==(2**m-1):
                ok=True
                ans=(dicta[i]+1,dicta[j]+1)
                break
        if ok ==True:
            break
    if ok==True:
        left=mid+1
    else:
        right=mid
    #print(dicta,mid,i,j)
print(*ans)
