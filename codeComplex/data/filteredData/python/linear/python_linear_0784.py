def main(n):
    # Deterministically generate input array of size n
    # Example pattern: a[i] = i//2 to force some duplicates, plus an offset pattern
    a = [(i // 2) for i in range(n)]

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
    # Example fixed-scale call for experimentation
    main(10)