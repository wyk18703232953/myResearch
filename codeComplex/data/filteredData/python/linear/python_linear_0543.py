def main(n):
    # n: length of the array xs
    if n <= 0:
        return 0

    # Deterministic data generation for xs
    # Mix of positive, zero, and negative with simple arithmetic
    xs = [(i * 2 % 7) - (i % 3) for i in range(n)]

    prefix = [-1 for _ in range(n)]
    suffix = [-1 for _ in range(n)]
    prefix[0] = 0
    pre_has_neg = [False for _ in range(n)]
    suffix[-1] = 0
    suf_has_neg = [False for _ in range(n)]

    for i in range(n):
        if i == 0:
            prefix[i] = xs[i]
        else:
            prefix[i] = prefix[i - 1] + xs[i]

    for i in reversed(range(n)):
        if i == n - 1:
            suffix[i] = xs[i]
        else:
            suffix[i] = suffix[i + 1] + xs[i]

    for i in range(n):
        if i == 0:
            pre_has_neg[i] = xs[i] <= 0
        else:
            pre_has_neg[i] = pre_has_neg[i - 1] or xs[i] <= 0

    for i in reversed(range(n)):
        if i == n - 1:
            suf_has_neg[i] = xs[i] <= 0
        else:
            suf_has_neg[i] = suf_has_neg[i + 1] or xs[i] <= 0

    prebignum = [None for _ in range(n)]
    sufbignum = [None for _ in range(n)]

    for i in range(n):
        if i == 0:
            prebignum[i] = xs[i]
        else:
            prebignum[i] = min(prebignum[i - 1], xs[i])

    for i in reversed(range(n)):
        if i == n - 1:
            sufbignum[i] = xs[i]
        else:
            sufbignum[i] = min(sufbignum[i + 1], xs[i])

    neg_pre = [100000 for _ in range(n)]
    neg_suf = [100000 for _ in range(n)]

    for i in range(n):
        if i == 0:
            neg_pre[i] = min(xs[i], -xs[i])
        else:
            neg_pre[i] = neg_pre[i - 1] + min(xs[i], -xs[i])

    for i in reversed(range(n)):
        if i == n - 1:
            neg_suf[i] = min(xs[i], -xs[i])
        else:
            neg_suf[i] = neg_suf[i + 1] + min(xs[i], -xs[i])

    ans = -100000000000000000
    for i in range(n):
        tans = xs[i]
        if i == 0:
            pass
        elif pre_has_neg[i - 1]:
            tans -= neg_pre[i - 1]
        else:
            tans += prefix[i - 1]
            tans -= prebignum[i - 1] * 2

        if i == n - 1:
            pass
        elif suf_has_neg[i + 1]:
            tans -= neg_suf[i + 1]
        else:
            tans += suffix[i + 1]
            tans -= sufbignum[i + 1] * 2

        if tans > ans:
            ans = tans

    print(ans)
    return ans


if __name__ == "__main__":
    # Example deterministic call
    main(10)