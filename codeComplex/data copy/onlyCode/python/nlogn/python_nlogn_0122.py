
n,m,k=map(int,input().split())
list1=list(map(int,input().split()))
list1.sort(reverse=True)
c=0
i=0

while(k<m and i<n):
    k+=list1[i]-1
    i+=1
    c+=1
if(k>=m):
    print(c)
else:
    print(-1)