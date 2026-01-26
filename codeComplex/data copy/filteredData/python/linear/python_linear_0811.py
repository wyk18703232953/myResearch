def main(n):
    # Generate deterministic input data of size n
    # Original input:
    # n
    # a[0] a[1] ... a[n-1]
    #
    # Here we construct a list a of length n with a simple deterministic pattern.
    # Pattern: a[i] = i % 5
    a = [i % 5 for i in range(n)]

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
        # Preserve original behavior (do nothing if condition not met)
        pass
if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10)