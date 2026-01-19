def main():
    n, k = map(int, input().split(' '))

    if(k > 2*n): 
        return(0)
    if(k == 2*n or k==1): 
        return(2)

    iguales = [0]*(k+1)
    diferentes = [0]*(k+1)

    iguales[1] = 2
    diferentes[2] = 2

    modulo = 998244353

    for i in range(1, n):
        auxigual = [0]*(k+1)
        auxdiff = [0]*(k+1)

        for j in range(1, k+1):
            auxigual[j] = (iguales[j] + iguales[j-1] + 2*diferentes[j]) % modulo

        for k in range(2, k+1):
            auxdiff[k] = (diferentes[k] + diferentes[k-2] + 2*iguales[k-1]) % modulo
        
        iguales = auxigual
        diferentes = auxdiff

    return((iguales[-1] + diferentes[-1]) % modulo)

print(main())
	 		   				 			 	 	          		