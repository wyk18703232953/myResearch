I=lambda:map(int,input().split())
n,m=I()
q={}
for i in range(1,n+1):q[i]=0
for i in I():q[i]+=1
print(min(q.values()))