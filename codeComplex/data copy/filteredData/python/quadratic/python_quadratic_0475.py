def main(n):
    # n: size of the input (length of l, r, res)
    if n <= 0:
        return

    # Deterministic generation of l and r based on n
    # l[i]: number of previous indices j<i with res[j]>res[i]
    # r[i]: number of later indices j>i with res[j]>res[i]
    # We construct a deterministic res first, then compute l and r
    res = [i % 5 for i in range(n)]

    l = [0] * n
    r = [0] * n

    for i in range(n):
        cnt = 0
        for j in range(i):
            if res[j] > res[i]:
                cnt += 1
        l[i] = cnt

    for i in range(n):
        cnt = 0
        for j in range(i + 1, n):
            if res[j] > res[i]:
                cnt += 1
        r[i] = cnt

    # Now run the original core logic using generated n, l, r
    res_check = [0] * n
    for i in range(n):
        res_check[i] = n - l[i] - r[i]

    for i in range(n):
        ok = 0
        for j in range(i):
            if res_check[j] > res_check[i]:
                ok += 1
        if ok != l[i]:
            # print("NO")
            pass
            return
        ok = 0
        for j in range(i + 1, n):
            if res_check[j] > res_check[i]:
                ok += 1
        if ok != r[i]:
            # print("NO")
            pass
            return

    # print("YES")
    pass
    # print(' '.join(map(str, res_check)))
    pass
if __name__ == "__main__":
    main(10)