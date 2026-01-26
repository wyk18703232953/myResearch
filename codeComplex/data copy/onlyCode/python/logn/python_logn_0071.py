string = input()
l, r = string.split()
l = int(l)
r = int(r)
p = l ^ r
x = 1
while x <= p:
    x = x << 1
print(x-1)

			    		 		 	   			 					 	