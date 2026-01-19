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
        auxigual, auxdiff = [0]*(k+1), [0]*(k+1)
        for j in range(k):
            auxigual[j+1] = (iguales[j+1] + iguales[j] + 2*diferentes[j+1]) % modulo
            if(j >= 1):
                auxdiff[j+1] = (diferentes[j+1] + diferentes[j-1] + 2*iguales[j]) % modulo
        
        iguales = auxigual
        diferentes = auxdiff

    return((iguales[-1] + diferentes[-1]) % modulo)

print(main())