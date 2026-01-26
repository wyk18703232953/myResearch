def main(n):
    # Interpret n as both the size of the initial array and the number of queries
    size = max(1, n)

    # Deterministically generate the initial array 'a' of length 'size'
    # Example pattern: a[i] = (i * 3 + 1) % 1000
    a = [((i * 3 + 1) % 1000) for i in range(size)]

    array = []
    array.append(a)

    # Build the XOR triangle structure as in the original program
    for _ in range(size - 1):
        prev = array[-1]
        aux = []
        for j in range(1, len(prev)):
            xor_val = prev[j - 1] ^ prev[j]
            aux.append(xor_val)
        array.append(aux)

    # Transform the triangle using the max rule as in the original program
    for j in range(1, len(array)):
        row = array[j]
        prev_row = array[j - 1]
        for k in range(len(row)):
            maximo = max(row[k], prev_row[k], prev_row[k + 1])
            row[k] = maximo

    # Deterministically generate query list aux2 of length 'size'
    # Use all valid intervals [l, r] with 1 <= l <= r <= size in a fixed pattern
    aux2 = []
    l = 1
    r = size
    # Simple deterministic pattern: shrink [l, r] from both ends until size queries
    for i in range(size):
        # Ensure l and r always in valid range and l <= r
        if l > r:
            l = 1
            r = size
        aux2.append((l, r))
        if i % 2 == 0:
            l += 1

        else:
            r -= 1
        if l < 1:
            l = 1
        if r > size:
            r = size

    # Process queries and print results
    for l, r in aux2:
        # Clip to valid boundaries just in case
        if l < 1:
            l = 1
        if r > size:
            r = size
        if l > r:
            l, r = r, l
        # print(str(array[r - l][l - 1]))
        pass
if __name__ == "__main__":
    main(5)