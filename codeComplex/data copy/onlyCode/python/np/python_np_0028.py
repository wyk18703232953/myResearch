import math
res = [0, 1, 0, 3, 0, 15, 0, 133, 0, 2025, 0, 37851, 0, 1030367, 0, 36362925, 0]
n = int(input())
print(res[n] * math.factorial(n) % (10 ** 9 + 7))

  	   						 	  				 	  						