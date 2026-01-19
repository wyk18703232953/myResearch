def main(n):
    # n: length of the array r
    maxv = 10**5
    mod = 10**9 + 7

    # Deterministically generate input array r of length n
    # Values are in [1, maxv] and follow a simple pattern
    if n <= 0:
        print(0)
        return
    r = [(i % maxv) + 1 for i in range(n)]

    dp = [0] * (maxv + 1)  # preserved though unused in original code
    cnt = [0] * (maxv + 1)
    tmp = [0] * (maxv + 1)

    for i in range(n):
        cnt[r[i]] += 1

    for i in range(1, maxv + 1):
        for j in range(2 * i, maxv + 1, i):
            cnt[i] += cnt[j]
        tmp[i] = pow(2, cnt[i], mod) - 1

    for i in range(maxv, 0, -1):
        for j in range(2 * i, maxv + 1, i):
            tmp[i] = (tmp[i] - tmp[j]) % mod

    print(tmp[1] % mod)


if __name__ == "__main__":
    # Example call for time-complexity experiments
    main(100000)