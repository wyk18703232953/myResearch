import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split(' ')))
Array = [a]
 
for i in range(n - 1):
    aux = []
    for j in range(1, len(Array[-1])):
        aux.append(Array[-1][j-1] ^ Array[-1][j])
    Array.append(aux)
 
for j in range(1, len(Array)):
    for k in range(len(Array[j])):
        Array[j][k] = max(Array[j][k], Array[j-1][k], Array[j - 1][k + 1])
 
q = int(sys.stdin.readline())
for i in range(q):
    l, r = map(int, sys.stdin.readline().split(' '))
    sys.stdout.write(str(Array[r - l][l - 1]) + '\n')
 					 	 			  		  			 		  	  	