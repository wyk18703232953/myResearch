def main(n):
    # n controls the size of the array a and the number of queries m
    # Generate a deterministic array a of length n
    a = [(i * 37 + 23) % (n + 7) for i in range(n)]

    # Initial parity: number of inversions in a
    parity = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[j] < a[i]:
                parity ^= 1

    # Let the number of queries m be n as well
    m = n

    # Deterministically generate m queries (l, r) within [1, n]
    # 1-based indices as in the original problem
    for i in range(m):
        l = (i % n) + 1
        r = ((i * 2) % n) + 1
        if l > r:
            l, r = r, l

        dist = (r - l + 1)
        pairs = (dist - 1) * dist // 2

        if pairs & 1:
            parity ^= 1

        if parity:
            # print("odd")
            pass

        else:
            # print("even")
            pass
if __name__ == "__main__":
    main(10)