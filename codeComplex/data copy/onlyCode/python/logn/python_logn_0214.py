# Really big number
# sum - x < s
"""
Se aumentamos um número em 1, a soma de seus dígitos aumenta em no máximo 1. Logo, não é possível que um número
x seja um Really Big Number e x + 1 não.
Podemos usar esse fato para achar o primeiro número no intervalo [1, n] que é um Really Big Number usando busca
binária.
"""
def somadig(x):
    soma = 0
    while x>0:
        soma += x%10
        x = x//10
    return soma    

def main():
    x,s = map(int,input().split())

    comeco = 9
    fim = x
    if comeco >= fim:
        print(0)
        return
    while fim>=comeco:
        meio = (fim+comeco)//2
        if meio - somadig(meio) >= s:
            if (meio-1) - somadig(meio-1)<s:
                print(x-(meio-1))
                return
            fim = meio-1
        else:
            comeco = meio+1        
    print(0)
    return       

main()