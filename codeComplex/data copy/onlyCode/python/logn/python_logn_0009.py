a, b = map(int, input().split())

bitxor = a^b

res = 1
while bitxor:
    bitxor >>= 1
    res <<= 1

print(res-1)

 		   		  		  		   	 	 			 			