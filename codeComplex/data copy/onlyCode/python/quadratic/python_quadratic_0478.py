n=int(input())
l=list(map(int,input().split()))
r=list(map(int,input().split()))

cost=[(l[i]+r[i],i) for i in range(n)]

cost.sort()

CANDIES=[None]*n
CANDIES[cost[0][1]]=n

candy=n
for i in range(1,n):
    if cost[i][0]==cost[i-1][0]:
        CANDIES[cost[i][1]]=candy
    else:
        candy-=1
        CANDIES[cost[i][1]]=candy

#print(CANDIES)

check=1    
for i in range(n):
    lc=0
    rc=0
    for j in range(i):
        if CANDIES[j]>CANDIES[i]:
            lc+=1
    for j in range(i+1,n):
        if CANDIES[j]>CANDIES[i]:
            rc+=1

    #print(i,lc,rc)

    if lc!=l[i] or rc!=r[i]:
        check=0

if check==1:
    print("YES")
    for c in CANDIES:
        print(c,end=" ")
    #print(CANDIES)
else:
    print("NO")
    #print(CANDIES)
          
    
