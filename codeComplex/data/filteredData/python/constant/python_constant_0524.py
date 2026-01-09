def main(n):
    # Map n to building floors in a deterministic way
    # Ensure non-negative floors and some spread
    x = n % 50
    y = (3 * n + 7) % 50
    z = (5 * n + 11) % 50

    # Map n to times t1, t2, t3 (positive integers)
    t1 = (n % 7) + 1
    t2 = (n % 5) + 1
    t3 = (n % 9) + 1

    stairs = abs(x - y) * t1
    lift = abs(z - x) * t2 + t3 + t3 + abs(x - y) * t2 + t3
    # print('YES' if lift <= stairs else 'NO')
    pass
if __name__ == "__main__":
    main(1000)