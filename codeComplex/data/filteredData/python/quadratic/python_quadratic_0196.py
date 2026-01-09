def main(n):
    # n controls both array length and query count for scalability
    length = max(1, n)
    m = max(1, n)

    # deterministic generation of initial array 'a[0]'
    base = [i ^ (i // 2) for i in range(1, length + 1)]

    # build a as list of lists
    a = [base]
    for i in range(1, length):
        prev = a[-1]
        row = [prev[j] ^ prev[j + 1] for j in range(len(prev) - 1)]
        a.append(row)

    for i in range(length - 1):
        prev = a[i]
        cur = a[i + 1]
        merged = [max(prev[j], prev[j + 1], cur[j]) for j in range(len(cur))]
        a[i + 1] = merged

    # deterministic queries: (l, r) with 1 <= l <= r <= length
    qur = []
    for i in range(m):
        l = (i % length) + 1
        r = length
        qur.append((l, r))

    out = []
    for l, r in qur:
        out.append(a[r - l][l - 1])

    for v in out:
        # print(v)
        pass
if __name__ == "__main__":
    main(10)