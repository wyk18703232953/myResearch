def main(n):
    # Deterministically generate a, b, c based on n
    a = n
    b = 2 * n
    c = n // 2

    t = a + b - c
    if c > a or c > b:
        # print(-1)
        pass
        return
    if n - t >= 1:
        # print(n - t)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)