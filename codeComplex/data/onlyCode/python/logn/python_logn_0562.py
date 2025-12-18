n,x,y=int(input())-1,1,9
while n>x*y:n,x,y=n-x*y,x+1,y*10
print(str(10**(x-1)+n//x)[n%x])