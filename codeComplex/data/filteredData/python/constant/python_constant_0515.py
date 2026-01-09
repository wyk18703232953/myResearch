def main(n):
    from math import sin, tan, cos  # kept to preserve original imports, though unused

    # Deterministically generate inputs based on n
    x = n
    y = n // 2
    z = n // 3 if n >= 3 else 0
    t1 = (n % 5) + 1
    t2 = (n % 7) + 1
    t3 = (n % 3) + 1

    if abs(x - z) * t2 + abs(x - y) * t2 + 3 * t3 <= abs(x - y) * t1:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)