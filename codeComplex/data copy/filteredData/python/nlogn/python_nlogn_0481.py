def main(n):
    # Deterministically map n to original parameters:
    # original: n (number of items to select), m (length of array A)
    # here we set:
    #   n_items = n
    #   m = 5 * n (array length scales linearly with n, and guarantees enough size)
    n_items = max(1, n)
    m = 5 * n_items

    # Deterministically generate array A of length m
    # Example pattern: A[i] = (i % (n_items // 2 + 1)) + 1
    # This creates repeated values with controlled frequencies
    if n_items == 1:
        A = [1] * m

    else:
        base = n_items // 2 + 1
        A = [(i % base) + 1 for i in range(m)]

    from collections import Counter
    C = Counter(A)

    def is_ok(x):
        cnt = 0
        for v in C.values():
            cnt += v // x
        return cnt >= n_items

    ok = 0
    ng = 1000
    while ok + 1 < ng:
        c = (ok + ng) // 2
        if is_ok(c):
            ok = c

        else:
            ng = c

    # print(ok)
    pass
if __name__ == "__main__":
    main(10)