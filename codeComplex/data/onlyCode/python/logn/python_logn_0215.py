def somaDigitos(x):
    resp = 0
    while x > 0:
        resp += x%10
        x = x//10
    return resp

def isReallyBigNumber(x):
    return x - somaDigitos(x) >= s

n, s = input().split(" ")
n = int(n)
s = int(s)


# x - somadigitos >= s
# calc: # big numbers <= n
count = 0

#busca binária

ini = 1
fim = n
i = 0
ans = False
while ini <= fim:
    meio = (ini + fim)//2
    if isReallyBigNumber(meio):
        ans = meio   #guarda o último meio True
        fim = meio - 1
    else:
        ini = meio + 1

if ans:
    print(n - ans + 1)
else:
    print(0)



#se x é Really Big Number, x+1 também é
#pois a soma dos dígitos aumenta em
#no máximo 1

#calcular o menor really big number
#com busca binária
