import math
k, n, s, p = map(int, input().split())
sheets = math.ceil(n/s) * k
print(math.ceil(sheets/p))
 	  										  	 		 				