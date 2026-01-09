def main(n):
    # Deterministically generate a, b, c based on n
    a = n + 3
    b = 2 * n + 1
    c = n // 2

    if c > a or c > b:
        # print(-1)
        pass

    else:
        val = n - ((a - c) + (b - c)) - c
        # print(val if val <= n and val > 0 else -1)
        pass
if __name__ == "__main__":
    main(10)