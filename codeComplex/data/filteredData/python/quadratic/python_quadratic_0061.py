def main(n):
    # Interpret n as array size; number of queries also set to n for scalability
    size = max(1, n)
    q = size

    # Deterministic array generation based on n
    # Example pattern: arr[i] = (i * 2 + 3) % (size + 5)
    arr = [(i * 2 + 3) % (size + 5) for i in range(size)]

    inv = 0

    # Original double loop to compute inversion parity
    for i in range(size):
        for j in range(size):
            if i < j and arr[i] > arr[j]:
                inv += 1
            inv = inv % 2

    # Deterministic generation of q queries (l, r) with 1-based indices
    # Ensure 1 <= l <= r <= size
    queries = []
    for k in range(q):
        l = (k % size) + 1
        r = ((k * 3) % size) + 1
        if l > r:
            l, r = r, l
        queries.append((l, r))

    for l, r in queries:
        diff = r - l
        s = diff // 2
        if diff % 2:
            s += 1
        inv = (inv + (s % 2)) % 2
        if inv:
            # print("odd")
            pass

        else:
            # print("even")
            pass
if __name__ == "__main__":
    main(10)