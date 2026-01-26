# encontrar o máximo xor entre um par que se encontra no intervalo [l,r]

def main():
    l,r = map(int,input().split())

    if l == r:
        print(0)
        return

    l = bin(l)[2:]
    r = bin(r)[2:]

    if len(l) == len(r):
        i = 1 #ambos começam com 1, não preciso checar
        while l[i] == r[i]:
            i += 1
        tam = len(l)-i
    else:
        tam = len(r)

    num = ""
    for i in range(tam):
        num += '1'

    print(int(num,2))    

main()