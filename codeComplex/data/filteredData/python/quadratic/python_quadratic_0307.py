def helper(n, k, l):
    res = 0
    for i in range(n - k + 1):
        base_seg = l[i:i + k]
        sm_bseg = sum(base_seg)
        ln_bseg = len(base_seg)
        ans = sm_bseg / ln_bseg

        for j in range(i + k, n):
            sm_bseg += l[j]
            ln_bseg += 1
            ans = max(ans, sm_bseg / ln_bseg)

        res = max(res, ans)

    return res


def main(n):
    if n < 2:
        n = 2
    k = max(1, n // 2)
    l = [(i * 3 + 1) % 1000 for i in range(n)]
    result = helper(n, k, l)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)