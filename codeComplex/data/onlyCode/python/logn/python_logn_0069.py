entrada = input().split()

l = int(entrada[0])
r = int(entrada[1])

pop = l ^ r
result = 1

while (result <= pop):
    result = result << 1

print(result - 1)
		  				  		 	  	    					 		