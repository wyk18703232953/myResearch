def main(n):
    # n controls the size of the list a; ensure at least 1 element
    if n <= 0:
        n = 1

    # Deterministically generate M and a
    M = 10 * n + 5
    # Strictly increasing sequence within [0, M)
    # a[i] = i * step, where step is chosen so that a[n-1] < M
    step = max(1, M // (2 * n))
    a = [i * step for i in range(n)]
    # Ensure last element is strictly less than M
    if a and a[-1] >= M:
        a[-1] = M - 1

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
    print(ans)


if __name__ == "__main__":
    main(5)