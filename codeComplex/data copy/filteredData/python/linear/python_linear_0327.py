def main(n):
    import math

    # Ensure n is non-negative
    if n < 0:
        n = 0

    # Deterministically construct M and array a based on n
    # M grows roughly linearly with n to keep intervals reasonable
    M = 3 * n + 5

    # Construct a strictly increasing sequence of length n inside (0, M)
    # a[0] = 0, a[1..n] in (0, M), a[n+1] = M
    # Use simple arithmetic so that values are deterministic and scaled by n.
    # When n == 0, this just creates [0, M].
    inner = [1 + (2 * i) for i in range(n)]
    # Clip values to be less than M to keep structure valid
    inner = [x if x < M else M - 1 for x in inner]

    a = [0] + inner + [M]

    t1 = []
    t2 = []
    for i in range(n + 1):
        if i % 2 == 0:
            t1.append(a[i + 1] - a[i])

        else:
            t2.append(a[i + 1] - a[i])
    t2.append(0)

    ans = sum(t1)
    p = 0
    q = sum(t2)
    for i in range(math.ceil(n / 2)):
        p = p + t1[i]
        q = q - t2[i - 1]
        ans = max(ans, p + q - 1)
    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)