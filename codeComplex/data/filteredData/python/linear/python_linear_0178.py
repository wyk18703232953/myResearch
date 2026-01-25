def main(n):
    # n: input size, used as the length of arrays a and t
    if n <= 0:
        print(0)
        return

    # Deterministic choice of k based on n, 1 <= k <= n
    k = max(1, n // 3)

    # Deterministic generation of arrays a and t of length n
    # a: positive integers with some pattern
    a = [(i * 7 + 3) % 100 + 1 for i in range(n)]
    # t: 0 or 1 pattern depending on i
    t = [1 if (i % 3 == 0 or i % 5 == 0) else 0 for i in range(n)]

    # Original core logic
    ans = sum(a[ii] for ii in range(n) if t[ii])
    bb = [a[ii] if t[ii] == 0 else 0 for ii in range(n)]
    ll = 0
    rr = k
    tmp = sws = sum(bb[:k])
    while rr < n:
        sws -= bb[ll]
        sws += bb[rr]
        ll += 1
        rr += 1
        tmp = max(tmp, sws)
    ans += tmp
    print(ans)


if __name__ == "__main__":
    # Example call; you can change 10 to other sizes for experiments
    main(10)