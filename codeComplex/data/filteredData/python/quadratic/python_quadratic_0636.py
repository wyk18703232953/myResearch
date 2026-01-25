def main(n):
    if n <= 0:
        print(0)
        return

    # Deterministically generate input:
    # Original program expects:
    # - first line: integer n
    # - second line: n integers
    # Here we map the external n to that same size and build an array of length n.
    arr = [(i + 1) * (i % 5 + 1) for i in range(n)]

    arr.sort()
    tmp = [-1] * n
    c = 1
    for i in range(n):
        if tmp[i] != -1:
            continue
        x = arr[i]
        for j in range(i, n):
            if arr[j] % x == 0:
                tmp[j] = c
        c += 1

    print(c - 1)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)