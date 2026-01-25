def main(n):
    # Interpret n as both the number of rows and columns for determinism
    # Ensure at least 1 row and 1 column
    n = max(1, int(n))
    m = n

    s = 0
    e = n - 1
    for i in range(n // 2):
        for j in range(m):
            print(s + 1, j + 1)
            print(e + 1, m - j)
        s += 1
        e -= 1
    if n % 2 == 1:
        s = n // 2
        for j in range(m // 2):
            print(s + 1, j + 1)
            print(s + 1, m - j)
        if m % 2 == 1:
            print(s + 1, m // 2 + 1)


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)