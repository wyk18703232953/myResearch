"""
Nome: Stefano Lopes Chiavegatto
RA: 1777224
Fonte: Algoritmo "Maximum XOR value of a pair from a range" - https://www.geeksforgeeks.org/maximum-xor-value-of-a-pair-from-a-range/
"""
  
lr = input()
lr_list = lr.split(" ")
l = int(lr_list[0])
r = int(lr_list[1])
xor = l ^ r

bms = 0
while xor != 0:
    bms = bms + 1
    xor = xor >> 1

maxxor = 0
dois = 1
while bms != 0:
    maxxor = maxxor + dois
    dois = dois << 1
    bms = bms - 1

print(maxxor) 
	  	 			 	  	 						 	   	 	 	