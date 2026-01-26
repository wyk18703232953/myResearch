def main(n):
    # n: length of array a
    if n <= 0:
        return

    # deterministic construction of array a
    a = [(i * 2 + (i // 3)) % (n + 5) for i in range(n)]

    # count inversions (same core logic)
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                cnt += 1
    even = (cnt % 2 == 0)

    # deterministic construction of queries
    # let q scale with n for time-complexity experiments
    q = max(1, n)
    ans = []
    for k in range(q):
        # generate a deterministic interval [l, r]
        # spread intervals over the array in a deterministic pattern
        l = (k * 7) % n
        r = (l + (k * 5) % n)
        if l > r:
            l, r = r, l
        # adjust to 1-based indices as in the original code
        l1, r1 = l + 1, r + 1

        length = r1 - l1 + 1
        pairs = length * (length - 1) // 2
        if pairs % 2 == 1:
            even = not even
        if even:
            ans.append("even")

        else:
            ans.append("odd")

    # print("\n".join(ans))
    pass
if __name__ == "__main__":
    # example deterministic call for experimentation
    main(10)