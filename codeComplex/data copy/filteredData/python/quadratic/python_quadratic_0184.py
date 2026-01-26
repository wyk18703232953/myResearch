def main(n):
    # n controls the size of the initial array and the number of queries
    if n <= 0:
        return

    # Deterministic construction of initial array 'a'
    # Example: a[i] = (i * i + i) % (n + 7)
    a = [(i * i + i) % (n + 7) for i in range(n)]

    array = []
    array.append(a)

    # Build the XOR levels as in the original code
    for _ in range(n - 1):
        aux = []
        for j in range(1, len(array[-1])):
            xor_val = array[-1][j - 1] ^ array[-1][j]
            aux.append(xor_val)
        array.append(aux)

    # Replace each element with max over related elements, as in original
    for j in range(1, len(array)):
        for k in range(len(array[j])):
            maximo = max(array[j][k], array[j - 1][k], array[j - 1][k + 1])
            array[j][k] = maximo

    # Deterministic generation of queries
    # We generate q = n queries; l and r satisfy 1 <= l <= r <= n
    q = n
    for i in range(q):
        # Example mapping: spread l over [1, n], r so that r >= l
        l = (i % n) + 1
        # r index depends on l and i, but always within [l, n]
        span = n - l + 1
        r = l + (i % span)
        # print(str(array[r - l][l - 1]))
        pass
if __name__ == "__main__":
    main(5)