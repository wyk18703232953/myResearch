def main(n):
    import bisect as bi

    # Define problem sizes based on n
    # Number of elements in array a
    num_a = max(1, n)
    # Number of queries
    q = max(1, n)

    # Deterministic construction of array a
    # a[i] = (i % 7) + 1 ensures all positive, small bounded values
    a = [(i % 7) + 1 for i in range(num_a)]

    # Deterministic construction of queries l
    # Make them vary but bounded in relation to sum(a)
    som = sum(a)
    if som == 0:
        som = 1
    l = [((i * 3) % som) + 1 for i in range(q)]

    # Original logic
    som = sum(a)
    e = 0
    p = []
    for i in a:
        e += i
        p.append(e)

    e = 0
    for i in l:
        e += i
        if e >= som:
            e = 0
        x = bi.bisect(p, e)
        # print(num_a - x)
        pass
if __name__ == "__main__":
    main(10)