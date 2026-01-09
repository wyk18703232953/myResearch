def main(n):
    # Generate deterministic binary strings a and b of length n
    # Example pattern: a[i] = (i % 2 == 0), b[i] = ((i // 2) % 2 == 0)
    a = [(i % 2 == 0) for i in range(n)]
    b = [((i // 2) % 2 == 0) for i in range(n)]

    res = 0
    i = 0
    while i + 1 < n:
        if a[i] != b[i] and a[i] != a[i+1] and b[i] != b[i+1]:
            a[i] = b[i]
            a[i+1] = b[i+1]
            res += 1
            i += 2

        else:
            i += 1

    for i in range(n):
        if a[i] != b[i]:
            res += 1

    # print(res)
    pass
if __name__ == "__main__":
    # Example call for time complexity experiment
    main(10)