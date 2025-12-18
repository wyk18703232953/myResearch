n=int(input())
xw=[list(map(int,input().split())) for _ in [0]*n]

ab=sorted([[x-w,x+w] for x,w in xw],key=lambda x:(x[1],x[0]))

k=ab[0][0]
cnt=0
for a,b in ab:
    if k<=a:
        cnt+=1
        k=b

print(cnt)