def main(n):
    # Generate deterministic data: n rows, each with 2 integers (as in original input)
    # Example pattern:
    # first value: i % (max(1, n // 3) to create some ties on first key
    # second value: (i * 2) % (max(1, n // 2)) + 1 to create variation on second key
    L = []
    base1 = max(1, n // 3)
    base2 = max(1, n // 2)
    for i in range(n):
        a = i % base1
        b = (i * 2) % base2 + 1
        L.append([a, b, i + 1])

    L.sort(key=lambda X: (X[0], -X[1], X[2]))

    X = 0
    for i in range(1, n):
        if L[i][1] <= L[i - 1][1]:
            print(L[i][2], L[i - 1][2])
            X = 1
            break
    if X == 0:
        print(-1, -1)


if __name__ == "__main__":
    main(10)