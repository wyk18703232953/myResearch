l, r = (int(x) for x in input().split())
limit = l ^ r

if limit != 0:
  limit = len(bin(limit)) - 2
  maxXor = '1' * limit
  print(int(maxXor, 2))
else:
  print(0)

	    			 	  			      			 	 		