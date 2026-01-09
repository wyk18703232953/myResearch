def main(n):
    # Interpret n as:
    # n: length of arrays a and t
    # k: window size, set deterministically as max(1, n//3)
    k = max(1, n // 3)

    # Deterministic generation of input arrays a and t
    # a: sequence of integers depending on i
    # t: binary flags, e.g., periodic pattern based on i
    a = [(i * 2 + 3) % (n + 7) + 1 for i in range(n)]
    t = [1 if (i % 3 == 0) else 0 for i in range(n)]

    ans = sum(a[ii] for ii in range(n) if t[ii])
    bb = [a[ii] if t[ii] == 0 else 0 for ii in range(n)]

    if k > n:
        k = n

    ll = 0
    rr = k
    sws = sum(bb[:k])
    tmp = sws
    while rr < n:
        sws -= bb[ll]
        sws += bb[rr]
        ll += 1
        rr += 1
        if sws > tmp:
            tmp = sws
    ans += tmp
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)