import math
n,d=map(int,input().split())
p=list(map(int,input().split()))
q=[]
for i in range(len(p)-1):
    q.append(abs(p[i+1]-p[i]))
count=0
##print(q)
for k in q:
    if k==2*d:
        count+=1
    elif k>=2*d:
        count+=2
##    print(k,"-",count)
##    print(count,math.floor(k/2),math.floor((k/2)/d)*2)
    
print(count+2)
