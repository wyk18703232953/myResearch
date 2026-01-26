# import sys
# sys.stdin=open("input.in","r")
# sys.stdout=open("ot.out","w")

A,B=map(int,input().split())
x,y,z=map(int,input().split())
summ=0
y1=0
b1=0
y1=(x*2)+y

b1=y+(3*z)

summ=0
if y1>A:
	summ+=y1-A
if b1>B:
	summ+=b1-B
print(summ)