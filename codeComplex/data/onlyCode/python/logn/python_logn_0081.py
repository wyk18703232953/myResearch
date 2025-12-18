# Fonte https://cs.stackexchange.com/questions/29508/finding-the-max-xor-of-two-numbers-in-an-interval-can-we-do-better-than-quadrat
l, r = [int(x) for x in input().split()]

q = l ^ r
a = 1
while q:
    q //=2
    a <<= 1
print(a-1)

 	 			 	 			    	 			 			 		 		