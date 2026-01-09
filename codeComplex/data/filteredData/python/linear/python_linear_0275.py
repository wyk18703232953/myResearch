def main(n):
    # Deterministically generate m, a, b based on n
    m = n + 1 if n > 0 else 1
    a = n % 10 + 1
    b = (n // 2) % 10 + 1

    z = (n % m) * b
    x = ((n // m + 1) * m - n) * a
    y = min(z, x)
    result = y if y > 0 else 0
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)