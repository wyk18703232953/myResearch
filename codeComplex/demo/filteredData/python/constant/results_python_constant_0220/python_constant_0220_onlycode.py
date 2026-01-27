a,b=map(int,input().split())
x,y,z=map(int,input().split())
if a < x*2+y:
    ry=x*2+y-a
else:
    ry=0
if b < y+z*3:
    rb=y+z*3-b
else:
    rb=0
print(ry+rb)