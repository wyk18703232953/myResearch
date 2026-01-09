def main(n):
    # Deterministic data generation: l is a list of length n
    # Mix of negative, zero, and positive integers
    l = [i - (n // 2) for i in range(n)]

    m = 0
    for i in range(n):
        if l[i] >= 0:
            l[i] = -l[i] - 1
    for i in range(n):
        if l[i] < 0:
            m += 1
    if m % 2 == 0:
        for i in range(n):
            # print(l[i], end=" ")
            pass

    else:
        maksi = -1000000000000
        for i in range(n):
            if abs(l[i]) > maksi:
                maksi = abs(l[i])
                mk = i
        l[mk] = -l[mk] - 1
        for i in range(n):
            # print(l[i], end=" ")
            pass
if __name__ == "__main__":
    main(10)