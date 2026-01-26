def main(n):
    # Map n to problem parameters:
    # n: length of array a
    # m: number of residue classes, chosen as max(1, n // 3)
    # k: step size, chosen in relation to n
    if n <= 0:
        # print(0)
        pass
        return

    m = max(1, n // 3)
    k = max(1, n // 5)

    # Deterministic construction of a
    # Example pattern: a[i] = (i * 2 + 3) % (n + 5) + 1
    a = [((i * 2 + 3) % (n + 5)) + 1 for i in range(n)]

    from itertools import accumulate

    als = []
    for i in range(m):
        ls = a[:]
        for j in range(n):
            if j % m == i:
                ls[j] -= k
        als.append(list(accumulate(ls)))
    ans = 0
    for i in range(m):
        ls = als[i]
        mn = 0
        anstmp = 0
        for j in range(n):
            if mn > ls[j]:
                mn = ls[j]
            if j % m == i:
                anstmp = max(anstmp, ls[j] - mn)
        ans = max(ans, anstmp)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)