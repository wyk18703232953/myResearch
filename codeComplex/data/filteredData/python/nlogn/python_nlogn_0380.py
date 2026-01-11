def main(n):
    import heapq

    # Map n to original parameters:
    # n: number of elements
    # k: parameter controlling heap size (choose deterministic function of n)
    if n <= 0:
        return
    k = n // 2

    # Deterministic generation of two lists of length n
    # These correspond to the two calls to lst() in the original code
    # First list: "pwr"
    pwr_list = [i % 7 for i in range(n)]
    # Second list: "cns"
    cns_list = [(i * 3 + 1) % 10 for i in range(n)]

    # Core logic from original code
    l = sorted(zip(pwr_list, cns_list, range(n)))
    h = []
    sm = 0
    ans = {}
    for i in range(n):
        pwr, cns, ind = l[i]
        sm += cns
        if len(h) > k:
            sm -= heapq.heappop(h)
        ans[ind] = sm
        heapq.heappush(h, cns)

    # Output in the same structure as original program
    out = []
    for i in range(n):
        out.append(str(ans[i]))
    # print(" ".join(out))
    pass
if __name__ == "__main__":
    main(10)