def main(n):
    # Generate deterministic input list of length n
    # Example pattern: l[i] = i - n//2
    l = [i - n // 2 for i in range(n)]

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
    # Example call for experiment; adjust n as needed
    main(10)