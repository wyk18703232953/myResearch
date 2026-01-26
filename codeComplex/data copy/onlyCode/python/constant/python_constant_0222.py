h,b = map(int,input().split())
x,y,z = map(int,input().split())
print(max(0,2*x+y-h)+max(0,3*z+y-b))