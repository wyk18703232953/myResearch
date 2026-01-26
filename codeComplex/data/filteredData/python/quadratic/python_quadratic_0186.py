def main(n):
    # Interpret n as the length of the initial array and number of queries
    if n <= 0:
        return

    # Deterministic construction of initial array 'a' of length n
    # Example pattern: a[i] = (i * 3 + 1) % (n + 7)
    a = [((i * 3 + 1) % (n + 7)) for i in range(n)]

    array = []
    array.append(a)

    for _ in range(n - 1):
        aux = []
        for j in range(1, len(array[-1])):
            xor_val = array[-1][j - 1] ^ array[-1][j]
            aux.append(xor_val)
        array.append(aux)

    for j in range(1, len(array)):
        for k in range(len(array[j])):
            maximo = max(array[j][k], array[j - 1][k], array[j - 1][k + 1])
            array[j][k] = maximo

    # Deterministic construction of q queries
    q = n
    aux2 = []
    for i in range(q):
        l = (i % n) + 1
        r = n
        if l > r:
            l, r = r, l
        aux2.append((l, r))

    for l, r in aux2:
        # print(str(array[r - l][l - 1]))
        pass
if __name__ == "__main__":
    main(10)