# your code goes here
import sys
n=int(input())
s=input()
s+=s
h=0
for i in range(n):
	if s[i]=='H':
		h+=1
ans=h
for i in range(n):
	c=0
	for j in range(i,i+h):
		if s[j]=='T':
			c+=1
	ans=min(ans,c)
print(ans)
	

	
	
	

 		 	 	  			 	 	  		 		  	  		