# Nome: Guilherme Lima Hernandez Rincão
# RA: 169052
# B - Adding Reversed Numbers

from operator import xor

r = list(map(int, input().split()))

ms = xor(r[0], r[1])

max = 0
sum = 1

while ms > 0:
    ms >>= 1
    max += sum
    sum <<= 1

print(max)

   			 			 	      		 		 			 			