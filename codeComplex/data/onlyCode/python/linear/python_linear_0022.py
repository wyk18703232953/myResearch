a = int(input())
b = list(map(int, input().split()))
c = [int(i % 2 == 0) for i in b]
if(c.count(1) == 1):
	print(c.index(1) + 1)
else:
	print(c.index(0) + 1)
	
		  	 		 	  	 	   		 			 	   		