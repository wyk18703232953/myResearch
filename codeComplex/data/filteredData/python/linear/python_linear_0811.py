def main(n):
    # Deterministic data generation: array a of length n
    # Example pattern: a[i] = (i // 2) % (n // 3 + 1) to create some duplicates
    if n <= 0:
        return
    base = n // 3 + 1
    a = [(i // 2) % base for i in range(n)]

    d = {}
    for ai in a:
        if ai in d:
            d[ai] += 1

        else:
            d[ai] = 1
    if max(d.values()) >= 3 or (0 in d and d[0] >= 2) or list(d.values()).count(2) >= 2:
        # print('cslnb')
        pass
        return
    for i in d:
        if d[i] == 2 and (i - 1) in d:
            # print('cslnb')
            pass
            return
    s = sum(a)
    if s >= n * (n - 1) // 2:
        if (s - n * (n - 1) // 2) % 2 == 0:
            # print('cslnb')
            pass

        else:
            # print('sjfnb')
            pass

    else:
        # original code: pass (no output) when s < n*(n-1)//2
        return


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10)