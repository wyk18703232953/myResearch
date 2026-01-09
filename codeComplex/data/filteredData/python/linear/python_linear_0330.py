def main(n):
    # Map n to:
    #   - number of positions: n
    #   - maximum value M: n * 3 (ensures gaps for logic to work)
    # Construct a strictly increasing list a of length n with values < M
    if n <= 0:
        return 0

    M = n * 3
    # Deterministic construction: a[i] = 2*i + 1, always < M for this choice
    a = [2 * i + 1 for i in range(n)]
    # Ensure values stay below M
    a = [x % (M - 1) for x in a]
    a.sort()
    # Ensure strictly increasing by fixing possible collisions
    for i in range(1, n):
        if a[i] <= a[i - 1]:
            a[i] = a[i - 1] + 1
    # Trim if any element hits or exceeds M
    a = [x for x in a if x < M]
    n = len(a)
    if n == 0:
        # print(0)
        pass
        return

    a.insert(0, 0)
    n += 1

    lit = [0] * (n + 1)
    for i in range(1, n):
        if i % 2 == 0:
            lit[i] = lit[i - 1]

        else:
            lit[i] = lit[i - 1] + a[i] - a[i - 1]
    if n % 2 == 0:
        lit[n] = lit[n - 1]

    else:
        lit[n] = lit[n - 1] + M - a[n - 1]

    ans = lit[n]
    for i in range(n):
        pre_lit = lit[i]
        post_lit = M - a[i] - (lit[n] - lit[i])
        if i > 0 and a[i - 1] + 1 < a[i]:
            if i % 2 == 0:
                ans = max(ans, pre_lit + 1 + post_lit)

            else:
                ans = max(ans, pre_lit - 1 + post_lit)
        if (i + 1 < n and a[i] + 1 < a[i + 1]) or (i + 1 == n and a[n - 1] + 1 < M):
            if i % 2 == 0:
                ans = max(ans, pre_lit + post_lit + 1)

            else:
                ans = max(ans, pre_lit + post_lit - 1)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)