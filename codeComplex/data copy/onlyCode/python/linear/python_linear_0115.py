# cook your dish here
import math
n=int(input())
if(n%2==0):
   x=math.floor(n/2+1)*(math.floor(n/2))
if(n%2!=0):
   x=(math.ceil(n/2)*(math.ceil(n/2)))
print(x)