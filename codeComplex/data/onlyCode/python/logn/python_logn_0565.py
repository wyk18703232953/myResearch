# your code goes here
N = int(input())
terms = 1
n = 9
total = 0
# 9, 90, 900, 9000 etc...
while N > terms*n:
	N = N - terms*n
	total = total + n
	terms=terms+1
	n = n*10
print(str(total+(N+terms-1)//terms)[(N-1)%terms])
  	  		 	   		 		  		        		