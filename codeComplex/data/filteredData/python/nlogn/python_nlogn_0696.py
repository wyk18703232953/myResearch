def main(n):
    # Deterministic data generation:
    # Original program expects:
    #   n: number of elements
    #   a: list of n integers
    # Here we generate a deterministically structured list of length n.
    # Example pattern: a[i] = (i // 2)
    a = [-1] + [i // 2 for i in range(n)]

    s = set()
    s.add(-1)
    a.sort()
    count, add = 0, 0
    flag = 0
    for i in range(1, n + 1):
        if a[i] in s and a[i] - 1 in s:
            flag = 1
            break
        if a[i] in s:
            add += 1
        if add == 2:
            flag = 1
            break
        s.add(a[i])
        count += a[i] - (i - 1)
    if flag == 0 and count % 2 == 1:
        print("sjfnb")
    else:
        print("cslnb")


if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)