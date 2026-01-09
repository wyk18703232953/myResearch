def main(n):
    # n: length of array a
    # Deterministically generate array a of length n
    a = [(i * 2 + 3) % (n + 7) for i in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                cnt += 1
    even = cnt % 2 == 0

    # Deterministically generate q and queries based on n
    q = max(1, n)  # number of queries
    ans = []
    for k in range(q):
        # Generate l, r such that 0 <= l <= r < n
        if n == 0:
            # Edge case: no elements, but keep behavior deterministic
            even = even  # no-op
            ans.append('even' if even else 'odd')
            continue
        l = k % n
        r = (k * 2 + 1) % n
        if l > r:
            l, r = r, l

        length = r - l + 1
        pairs = length * (length - 1) // 2
        if pairs % 2 == 1:
            even = not even
        if even:
            ans.append('even')

        else:
            ans.append('odd')

    # print('\n'.join(ans))
    pass
if __name__ == "__main__":
    main(5)