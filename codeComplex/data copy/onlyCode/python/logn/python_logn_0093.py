#Problem A - Little Girl and Maximum XOR

numeros = [int(i) for i in input().split(' ')]

l = bin(numeros[0])
r = bin(numeros[1])

p = -1

if (len(r) == len(l)):
    for i in range (len(l)):
        if (l[i] != r[i]):
            p = i
            break
    if(numeros[0] != numeros[1]):
        saida = 2**(len(r) - p) - 1
        print(saida)
    else:
        print(0)

else:
    if(numeros[0] != numeros[1]):
        saida = 2**(len(r) - 2) - 1
        print(saida)
    else:
        print(0)
 		   	  						 	 	  			  	