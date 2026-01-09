def main(n):
    # Interpret n as both:
    # - the size of the initial array a (length n)
    # - the number of queries q (also n)
    # Deterministic construction of a: a[i] = (i % 7) ^ (i // 3)
    a = [((i % 7) ^ (i // 3)) for i in range(n)]
    array = []
    array.append(a)

    for _ in range(n - 1):
        aux = []
        for j in range(1, len(array[-1])):
            xor_val = (array[-1][j - 1] ^ array[-1][j])
            aux.append(xor_val)
        array.append(aux)

    for j in range(1, len(array)):
        for k in range(len(array[j])):
            maximo = max(array[j][k], array[j - 1][k], array[j - 1][k + 1])
            array[j][k] = maximo

    # Deterministic generation of q = n queries (l, r) with 1 <= l <= r <= n
    # Example pattern: intervals of increasing length, wrapped within [1, n]
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