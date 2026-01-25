def main(n):
    # Generate deterministic input of size n
    # Original program: first line n, second line n integers
    # Here we ignore the first input value (n) in logic because original code does too
    # We generate the list of integers deterministically based on n
    arr = [(i * (-1 if i % 2 == 0 else 1)) for i in range(1, n + 1)]

    a = []
    for i in arr:
        if abs(-i - 1) > abs(i):
            a.append(-i - 1)
        else:
            a.append(i)

    c = 0
    for i in a:
        if i < 0:
            c += 1
    if c % 2:
        me = 0
        for i in range(len(a)):
            if a[i] < a[me]:
                me = i
        a[me] = -a[me] - 1

    # Preserve original output format: space-separated on one line
    print(*a)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)