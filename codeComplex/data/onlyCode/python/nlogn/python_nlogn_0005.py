import math
n,t=map(int,input().split())
l=[]
for _ in range(n):
    a,b=map(int,input().split())
    x=a-b/2
    y=a+b/2
    l.append([x,y])
l.sort()
c=0
 
for i in range(n-1):
    if(l[i+1][0]-l[i][1]>t):
        c+=2
    elif(l[i+1][0]-l[i][1]==t):
        c+=1
print(c+2)
    