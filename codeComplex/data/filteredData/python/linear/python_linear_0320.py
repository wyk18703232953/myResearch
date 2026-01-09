def main(n):
    # Generate deterministic input data based on n
    # l1: ["s0", "s1", ..., "s(n-1)"]
    l1 = ["s" + str(i) for i in range(n)]
    # l2: first half same as l1, second half shifted by 1
    l2 = ["s" + str(i) for i in range(n // 2)] + ["s" + str((i + 1) % n) for i in range(n // 2, n)]

    c = 0
    for i in range(n):
        if l1[i] in l2:
            l2.remove(l1[i])

        else:
            c += 1
    # print(c)
    pass
if __name__ == "__main__":
    main(10)