# import sys
# input=sys.stdin.readline


n,a,b=list(map(int,input().split()))
d=[]
for i in range(n):
    d.append(["1"]*n)
    d[i][i]="0"
if [n,a,b]==[2,1,1]:
    print("NO")
elif [n,a,b]==[3,1,1]:
    print("NO")
elif a==1:
    c=n-b
    for i in range(c):
        d[i][i+1]="0"
        d[i+1][i]="0"
    print("YES")
    for i in range(n):
        print("".join(d[i]))
elif a!=1 and b!=1:
    print("NO")
else:
    print("YES")
    for i in range(a-1):
        for j in range(n):
            d[i][j]="0"
        for j in range(n):
            d[j][i]="0"
    for i in range(n):
        print("".join(d[i]))