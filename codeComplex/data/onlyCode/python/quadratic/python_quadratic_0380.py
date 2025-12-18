n,m=map(int,input().split())
l=[]
for i in range(n):
    s=input()
    l.append(s)
minX,minY,maxX,maxY=n,m,0,0
for i in range(n):
    for j in range(m):
        if l[i][j]=='B':
            minX,minY,maxX,maxY=min(minX,i),min(minY,j),max(maxX,i),max(maxY,j)
print((minX+maxX)//2+1,(minY+maxY)//2+1)