import math



n,k = map(int,input().split())
l=[]
c=0
for j in range(2,n):
    p=0

    for i in range(2,int(math.sqrt(j))+1):

        if j%i==0:

            p=1
            break
        else:
            pass

    if p==0:
        l.append(j)

l+=[n]

for i in range(len(l)-1):

    if (l[i]+l[i+1]+1) in l:

        c+=1
if c>=k:
    print("YES")
else:
    print("NO")
