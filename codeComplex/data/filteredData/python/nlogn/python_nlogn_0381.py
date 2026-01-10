def main(n):
    # Interpret n as the number of elements; choose a deterministic k
    if n <= 0:
        return
    k = n // 3  # deterministic choice based on n

    # Deterministically generate input lists of length n
    # pwr list and cns list (same structure as two lst() calls)
    pwr_list = [i % 10 for i in range(n)]
    cns_list = [(i * 2) % 7 + 1 for i in range(n)]

    # Core logic preserved
    l = sorted(zip(pwr_list, cns_list, range(n)))
    h = []
    sm = 0
    ans = {}
    for i in range(n):
        pwr, cns, ind = l[i]
        sm += cns
        if len(h) > k:
            p = 0
            for j in range(len(h)):
                if h[p] > h[j]:
                    p = j
            sm -= h.pop(p)
        ans[ind] = sm
        h += [cns]

    # Output as in original program
    out = []
    for i in range(n):
        out.append(str(ans[i]))
    print(' '.join(out))


if __name__ == "__main__":
    main(10)