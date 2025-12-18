yellow,blue = map(int,input().split())
x,y,z = map(int,input().split())
ry = x*2+y
rb =z*3+y
r1,r2 = 0,0
if ry-yellow < 0:
    r1 = 0
else:
    r1 = ry-yellow
if rb - blue < 0:
    r2 = 0
else:
    r2 = rb-blue
print(r1+r2)
