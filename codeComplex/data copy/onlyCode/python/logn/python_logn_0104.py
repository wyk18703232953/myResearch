l,r=map(int,input().split())
lxr = l^r 
msb = 0
while(lxr):
	msb+= 1
	lxr>>= 1
m = 0
t=1
while msb:
	m += t
	t <<= 1
	msb -= 1
print(m)
 	 		 						   	 	   						 		