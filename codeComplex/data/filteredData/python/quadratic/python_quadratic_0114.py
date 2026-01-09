def main(n):
    # n corresponds to the number of elements m in the original problem
    # we fix the value of "n_original" deterministically as n//2 + 1 (at least 1)
    n_original = n // 2 + 1
    if n_original < 1:
        n_original = 1
    m = n

    # deterministically generate c of length m with values in [1, n_original]
    # pattern: c[i] = (i % n_original) + 1
    c = [(i % n_original) + 1 for i in range(m)]

    aa = [0] * (n_original + 1)
    for cc in c:
        aa[cc] += 1
    result = min(aa[1:])
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)