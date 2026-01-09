def main(n):
    # Interpret n as both the length of the initial array and the number of queries
    size = n
    q = n

    # Deterministic generation of initial array 'a' of length 'size'
    # Example pattern: a[i] = (i * 3) ^ (i + 5)
    a = [(i * 3) ^ (i + 5) for i in range(1, size + 1)]

    array = []
    array.append(a)

    # Build XOR triangle
    for i in range(size - 1):
        aux = []
        last = array[-1]
        for j in range(1, len(last)):
            xor_val = last[j - 1] ^ last[j]
            aux.append(xor_val)
        array.append(aux)

    # Transform with max operation
    for j in range(1, len(array)):
        for k in range(len(array[j])):
            maximo = max(array[j][k], array[j - 1][k], array[j - 1][k + 1])
            array[j][k] = maximo

    # Deterministic generation of q queries (l, r)
    # Ensure 1 <= l <= r <= size
    queries = []
    for i in range(1, q + 1):
        l = (i % size) + 1
        r = size - (i % size)
        if l > r:
            l, r = r, l
        if l == 0:
            l = 1
        if r < l:
            r = l
        if r > size:
            r = size
        queries.append((l, r))

    # Execute queries and print results
    for l, r in queries:
        # print(str(array[r - l][l - 1]))
        pass
if __name__ == "__main__":
    main(10)