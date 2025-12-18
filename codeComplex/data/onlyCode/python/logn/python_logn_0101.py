a,b = map(int,input().split())
a = a^b
k = 0
while a:
	k += 1
	a = a>>1
print(2**k-1)
		  			 	   	 			  								   	