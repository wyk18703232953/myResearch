line = input().split()
l = int(line[0])
r = int(line[1])

diff = (r ^ l)
print(pow(2, diff.bit_length()) - 1)
	 						  			  	     	 	 						