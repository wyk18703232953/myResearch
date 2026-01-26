def main(n):
    # n controls the length of array a; number of queries q is also set to n
    if n <= 0:
        return

    # deterministic array generation: a[i] = (i * 2 + 1) % (n + 3)
    a = [(i * 2 + 1) % (n + 3) for i in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                cnt += 1
    even = cnt % 2 == 0

    q = n
    ans = []
    for t in range(q):
        # deterministic queries:
        # l, r are 1-based in the original code, keep that structure.
        # Make intervals of varying length but always valid.
        l = (t % n) + 1
        r = ((t * 3) % n) + 1
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
    main(10)