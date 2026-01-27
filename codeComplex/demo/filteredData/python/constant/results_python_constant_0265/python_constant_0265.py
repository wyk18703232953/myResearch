def main(n):
    # Deterministically generate p, l, r based on n
    # Ensure 1 <= l <= p <= r <= n
    if n < 3:
        # Handle small n deterministically
        p = 1
        l = 1
        r = n

    else:
        p = (n // 2) + 1
        l = max(1, p - (n // 3))
        r = min(n, p + (n // 3))
        if l > p:
            l = p
        if r < p:
            r = p
    if l == 1 and r == n:
        result = 0
    elif l == 1:
        result = abs(p - r) + 1
    elif r == n:
        result = abs(p - l) + 1

    else:
        result = min(abs(p - l), abs(p - r)) + r - l + 2
    # print(result)
    pass
if __name__ == "__main__":
    main(10)