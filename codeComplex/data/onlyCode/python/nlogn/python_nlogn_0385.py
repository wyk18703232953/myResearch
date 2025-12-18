from heapq import *

n,k=map(int,input().split())
p=[int(X) for X in input().split()]
c=[int(x) for x in input().split()]
p=[[p[i],c[i],i] for i in range(n)]
p.sort()
j=0
an=[0]*n
an[p[0][2]]=p[0][1]
z=[]
heapify(z)
#print(p)
for i in range(1,n):

     s=p[i][1]
     if p[i][0]!=p[i-1][0]:
         while (j<i):

             heappush(z,(-1)*p[j][1])
             j+=1

     tt=[]
     for __ in range(k):

         tt.append(heappop(z))
         if not z:
             break
     #print(tt,i,j)
     for v in tt:
         s+=abs(v)
         heappush(z, v )
     #print(s)
     an[p[i][2]]=s

print(*an)

