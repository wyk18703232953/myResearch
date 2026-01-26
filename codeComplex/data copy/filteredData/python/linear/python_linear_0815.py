def main(n):
    # Generate deterministic input data based on n
    # Original program:
    # n: number of elements
    # a: list of n integers
    #
    # Here we choose a deterministic pattern that can create:
    # - no duplicates
    # - some duplicates
    # depending on n, to exercise the logic while staying fully deterministic.
    #
    # For simplicity, let a[i] = i // 2, giving controlled duplicates,
    # but still well-defined for any n.
    a = [i // 2 for i in range(n)]

    total = sum(a)
    final = n * (n - 1) // 2
    repeated = []
    count = {}

    for i in a:
        try:
            count[i] += 1
            repeated.append(i)
        except KeyError:
            count[i] = 1

    moves = total - final

    if len(repeated) > 1:
        # print('cslnb')
        pass
    elif 0 in repeated:
        # print('cslnb')
        pass
    elif len(repeated) == 1 and repeated[0] - 1 in a:
        # print('cslnb')
        pass

    else:
        if moves % 2 == 0 or moves <= 0:
            # print('cslnb')
            pass

        else:
            # print('sjfnb')
            pass
if __name__ == "__main__":
    # Example deterministic calls for different scales
    main(1)
    main(5)
    main(10)