def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    array = []
    array.append(a)

    for i in range(n - 1):
        aux = []
        for j in range(1, len(array[-1])):
            xor = (array[-1][j-1] ^ array[-1][j])
            aux.append(xor)
        array.append(aux)

    for j in range(1, len(array)):
        for k in range(len(array[j])):
            maximo = max(array[j][k], array[j-1][k], array[j-1][k+1])
            array[j][k] = maximo

    q = int(input())
    aux2 = []

    for i in range(q):
        l, r = map(int, input().split(' '))
        aux2.append((l, r))

    for i in aux2:
        l, r = i[0], i[1]
        print(str(array[r-l][l-1]))

main()