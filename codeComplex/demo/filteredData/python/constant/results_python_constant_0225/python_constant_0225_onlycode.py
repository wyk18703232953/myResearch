
# import os
 
a,b = map(int,input().split())
 
x,y,z=map(int,input().split())
 
r = 0

yellow = 2*x
blue = 3*z
green = y

if a > yellow:
    a -= yellow
else:
    r += abs(a-yellow)
    a=0

if b > blue:
    b -= blue
else:
    r += abs(b-blue)
    b=0

if a > green:
    a-= green
else:
    r += abs(a-green)

if b > green:
    b-=green
else:
    r += abs(b-green)

print(r)