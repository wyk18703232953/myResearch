l,r=map(int,input().split())
z=l^r
c=0
if(z==0):
    print(0)
    exit()
while(z):
	c+=1;
	z>>=1;
x='1'*c
print(int(x,2))
	   	  	   		 	 		  	 	  		  		