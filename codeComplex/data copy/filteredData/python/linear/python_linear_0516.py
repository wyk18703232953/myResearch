def main(n):
    # Ensure n is at least 2 so that range(n-1) makes sense
    if n < 2:
        n = 2

    # Deterministically generate a and b based on n
    # a: pattern of 0,1,0,1,...
    # b: shifted pattern of 1,0,1,0,...
    a = [i % 2 for i in range(n)]
    b = [(i + 1) % 2 for i in range(n)]

    res = 0

    for j in range(n - 1):
        if (a[j] == 0) and (a[j + 1] == 1) and (b[j] == 1) and (b[j + 1] == 0):
            res += 1
            a[j] = 1
            a[j + 1] = 0

        elif (a[j] == 1) and (a[j + 1] == 0) and (b[j] == 0) and (b[j + 1] == 1):
            res += 1
            a[j] = 0
            a[j + 1] = 1

    for j in range(n):
        if a[j] != b[j]:
            res += 1

    # print(res)
    pass
if __name__ == "__main__":
    # Example deterministic run for a chosen n
    main(10)