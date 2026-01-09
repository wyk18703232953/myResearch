def main(n):
    # Interpret n as the upper bounds A and B and also as base for x, y, z
    A = n
    B = n

    # Deterministically generate x, y, z from n
    x = n
    y = n // 2
    z = n % 7

    summ = 0
    y1 = (x * 2) + y
    b1 = y + (3 * z)

    if y1 > A:
        summ += y1 - A
    if b1 > B:
        summ += b1 - B

    # print(summ)
    pass
if __name__ == "__main__":
    main(10)