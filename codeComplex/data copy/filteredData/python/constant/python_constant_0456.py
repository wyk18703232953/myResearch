def main(n):
    # Interpret n as the maximum coordinate value (grid size n x n)
    # Deterministically generate points A, B, C based on n
    # Ensure n >= 3 to have some spread; if smaller, fall back to simple case
    if n < 3:
        ax, ay = 0, 0
        bx, by = 1, 1
        cx, cy = 2, 2

    else:
        ax, ay = 1, 1
        bx, by = n // 2, n // 3
        cx, cy = (n * 2) // 3, (n * 2) // 3

    if ((cx < ax) == (bx < ax)) and ((cy < ay) == (by < ay)):
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)