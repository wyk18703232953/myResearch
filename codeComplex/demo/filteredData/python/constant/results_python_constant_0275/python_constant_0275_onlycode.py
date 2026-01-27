import math
num=int(input())
k=math.ceil(num/2)
if num%2==0:
    print(k+1)
else:
    print(k)