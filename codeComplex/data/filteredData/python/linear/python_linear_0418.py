def main(n):
    # Deterministic input generation
    # Original input:
    # n, x
    # b (list of n integers)
    #
    # Here we fix x deterministically and generate b based on n.
    x = (n * 3 + 5)  # deterministic x depending on n
    b = [(i * 2 + (i // 3)) & ((1 << 20) - 1) for i in range(1, n + 1)]

    d = {}
    flag = 0
    for i in b:
        if d.get(i):
            flag = 1
            break

        else:
            d[i] = 1
    if flag:
        # print(0)
        pass

    else:
        flag = 0
        c = set()
        for i in b:
            a = i & x
            c.add(a)
            if d.get(a) and a != i:
                flag = 1
                break
        if flag:
            # print(1)
            pass
        elif len(c) < n and flag == 0:
            # print(2)
            pass

        else:
            # print(-1)
            pass
if __name__ == "__main__":
    main(10)