def main(n):
    # Interpret n as the magnitude scale for a, b, x, y, z
    # Deterministic construction based on n
    a = n * 3 + 1
    b = n * 4 + 2
    x = n + 1
    y = n // 2 + 1
    z = n % 5 + 1

    ans = 0
    p = a - ((x * 2) + y)
    q = b - ((z * 3) + y)

    if p < 0 and q < 0:
        ans = abs(p) + abs(q)
    elif p < 0:
        ans = abs(p)
    elif q < 0:
        ans = abs(q)

    else:
        ans = 0

    return ans


if __name__ == "__main__":
    # Example deterministic call
    result = main(10)
    # print(result)
    pass