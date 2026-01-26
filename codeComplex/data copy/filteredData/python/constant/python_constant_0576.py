def main(n):
    # Deterministically generate x, y based on n
    x = n // 2 + 1
    y = n // 3 + 1
    if x > n:
        x = n
    if y > n:
        y = n

    na = abs(x - 1) + abs(y - 1)
    nb = abs(n - x) + abs(n - y)
    if na <= nb:
        # print("white")
        pass

    else:
        # print("black")
        pass
if __name__ == "__main__":
    main(10)