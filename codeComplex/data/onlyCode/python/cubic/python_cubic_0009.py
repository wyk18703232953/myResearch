
cadena = input()
n = len(cadena)

rpta = 0

for i in range(n-1):
    tamanho_cadena = n-i-1
    for j in range(n-tamanho_cadena):
        subcadena = cadena[j:j+tamanho_cadena]
        contador = 1
        for k in range(n-tamanho_cadena-j):
            if subcadena == cadena[j+k+1:j+k+1+tamanho_cadena]:
                contador = contador + 1
        if contador >=2  and rpta == 0:
            rpta = tamanho_cadena
    if rpta !=0:
        break

print(rpta)