def main(n):
    if n <= 0:
        # print(0)
        pass
        return

    # Set length of arrays; ensure at least 1
    m = n

    # Deterministically generate c and a
    # c: some varying positive integers
    c = [(i * 7 + 3) % 100 + 1 for i in range(m)]

    # a: permutation-like mapping 1..m forming cycles deterministically
    # Example: rotate by 1 position
    a = [(i + 1) % m + 1 for i in range(m)]

    u = [0] * len(a)
    ans = 0

    for i in range(len(a)):
        if u[i] != 0:
            continue
        idx = i
        while u[idx] == 0:
            u[idx] = 1
            idx = a[idx] - 1

        if u[idx] == 2:
            idx = i
            while u[idx] == 1:
                u[idx] = 2
                idx = a[idx] - 1
            continue

        start = idx
        mn = c[idx]
        u[idx] = 2
        while a[idx] - 1 != start:
            idx = a[idx] - 1
            mn = min(mn, c[idx])
            u[idx] = 2

        idx = i
        while u[idx] == 1:
            u[idx] = 2
            idx = a[idx] - 1
        ans += mn
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)