(x, y) = list(map(int, input().split(' ')))

a = 0
b = x * y
pos = True

for t in reversed(range(b)):
    b -= 1
    print(str(int(a / y + 1)) + ' '+ str(int(a % y + 1)))
    a += b * (1 if pos else -1)
    pos = not pos  

   			 								 		 			  	    	