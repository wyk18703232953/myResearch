import math
k,n,s,p=[int(x) for x in input().split()]
x=math.ceil(n/s)
y=math.ceil(x*k/p)
print(y)