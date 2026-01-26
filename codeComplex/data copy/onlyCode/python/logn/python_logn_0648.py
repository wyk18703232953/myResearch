def wzor(n):
    return (n*(n+1))/2

def mafia():
    pom = [int(x) for x in input().split()]
    n = pom[0]
    c = pom[1]

    po = 1
    ko = n
    sr = (po + ko)//2
    while po != ko:
        if wzor(sr)-(n-sr) >= c:
            ko = sr
        else:
            po = sr+1
        sr = (po+ko)//2

        
    print(int(wzor(po)-c))

mafia()
