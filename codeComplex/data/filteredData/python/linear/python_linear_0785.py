def main(n):
    # Deterministically generate input array `a` of length n
    # Ensure it may contain duplicates and zeros, to exercise all branches.
    # Example scheme: a[i] = (i // 2) % max(1, n//3 + 1)
    if n <= 0:
        a = []

    else:
        mod_base = max(1, n // 3 + 1)
        a = [ (i // 2) % mod_base for i in range(n) ]

    a = sorted(a)
    duplicates = {}
    d = None
    delta = 0
    for i, el in enumerate(a, 1):
        if el not in duplicates:
            duplicates[el] = 0

        else:
            d = el
            duplicates[el] += 1
        min_value = i - 1
        delta += el - min_value

    if sum(duplicates.values()) > 1 or duplicates.get(0, 0) >= 1 or (d is not None and d - 1 in duplicates):
        # print('cslnb')
        pass
    elif delta == 0:
        # print('cslnb')
        pass
    elif delta % 2 == 1:
        # print('sjfnb')
        pass

    else:
        # print('cslnb')
        pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)