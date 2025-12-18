import math

n=int(input())
a=list(map(int ,input().split()))
x=10**9+2
y=0
for i in range(n):
    if(x>math.ceil((a[i]-i)/n)*n+i+1):
        x=math.ceil((a[i]-i)/n)*n+i+1
        y=i+1
print(y)