a=[]
n=int(input())
for i in range(n):
    l,r=map(int,input().split())
    a.append([l,r,i+1])
a.sort(key=lambda x:(x[0],-x[1]))
r=0
iid=0
f=1
for i in range(n):
    if(r>=a[i][1]):
        f=0
        print(a[i][2],a[iid][2])
        break;
    else:
        r=a[i][1]
        iid=i;
if(f):
    print("-1 -1")
