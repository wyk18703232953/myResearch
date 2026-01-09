def main(n):
    from operator import xor

    # Interpret n as both the length of the initial array and the number of queries
    length = n
    m = n

    # Deterministically generate the initial array a[0]
    # Here: a[0][i] = (i + 1) ^ (i // 2)
    base_row = [(i + 1) ^ (i // 2) for i in range(length)]
    a = [base_row]

    # Deterministically generate m queries (l, r) with 1 <= l <= r <= n
    # Pattern ensures coverage and determinism
    qur = []
    for i in range(1, m + 1):
        l = (i % length) + 1
        r = length - (i % length)
        if l > r:
            l, r = r, l
        if l == 0:
            l = 1
        if r < l:
            r = l
        qur.append([l, r])

    out = []

    # Build XOR layers
    for i in range(1, length):
        prev = a[-1]
        a.append([xor(prev[j], prev[j + 1]) for j in range(len(prev) - 1)])

    # Transform to max over intervals
    for i in range(length - 1):
        row_i = a[i]
        row_next = a[i + 1]
        a[i + 1] = [max(row_i[j], row_i[j + 1], row_next[j]) for j in range(len(row_next))]

    # Answer queries
    for l, r in qur:
        out.append(a[r - l][l - 1])

    for v in out:
        # print(v)
        pass
if __name__ == "__main__":
    main(10)