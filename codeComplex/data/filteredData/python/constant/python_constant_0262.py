def main(n):
    # Deterministically generate p, l, r based on n
    # Ensure 1 <= l <= p <= r <= n
    if n < 3:
        # For very small n, fall back to trivial values
        p, l, r = 1, 1, n

    else:
        p = (n // 2) + 1
        l = 1
        r = n

    if l == 1 and r == n:
        result = 0
    elif l == 1:
        result = abs(p - r) + 1
    elif r == n:
        result = abs(p - l) + 1

    else:
        result = min(abs(p - r), abs(p - l)) + r - l + 2

    # print(result)
    pass
if __name__ == "__main__":
    main(10)