def main(n):
    # Deterministically generate x, y, z, t1, t2, t3 based on n
    x = n
    y = n // 2
    z = n % 10
    t1 = (n % 5) + 1
    t2 = (n % 7) + 1
    t3 = (n % 3) + 1

    a = abs(x - y) * t1
    b = abs(x - z) * t2 + abs(x - y) * t2 + t3 * 3
    if a < b:
        # print('NO')
        pass

    else:
        # print('YES')
        pass
if __name__ == "__main__":
    main(10)