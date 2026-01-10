import math

def main(n):
    lista = [i % 5 + 1 for i in range(1, n + 1)]
    pap = lista[:]
    pap.sort()
    if pap[-1] == 1:
        pap[-1] = 2
    else:
        pap = [1] + pap[:-1]
    for i in range(n):
        print(pap[i], end=" ")
    print()

if __name__ == "__main__":
    main(10)