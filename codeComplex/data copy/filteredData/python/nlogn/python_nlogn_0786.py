def main(n):
    # Interpret n as the length of array a
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministically generate k and array a of length n
    # Ensure 1 <= k <= n
    k = n // 3 + 1
    if k > n:
        k = n

    # Deterministic construction of a: strictly increasing sequence
    a = [i * 2 for i in range(n)]

    # Core logic from original program
    d = [a[i + 1] - a[i] for i in range(n - 1)]
    if k >= n:
        ans = 0

    else:
        ans = sum(sorted(d)[:n - 1 - (k - 1)])
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)