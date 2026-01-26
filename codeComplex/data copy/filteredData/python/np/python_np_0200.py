def main(n):
    # Map n to problem parameters deterministically
    # Ensure at least 2 elements to make the original logic meaningful
    if n < 2:
        n = 2

    # Define l, r, x deterministically based on n
    l = n
    r = n * (n + 1) // 2  # sum of 1..n
    x = max(1, n // 3)

    # Deterministically generate c as a list of n increasing integers
    c = [i + 1 for i in range(n)]

    ans = 0
    for bitmask in range(2 ** n):
        if bin(bitmask).count("1") > 1:
            res, _min, _max = 0, float("+inf"), float("-inf")
            for i, c_i in enumerate(c):
                bit_i = (bitmask >> i) & 1
                if bit_i:
                    res += c_i * bit_i
                    if c_i < _min:
                        _min = c_i
                    if c_i > _max:
                        _max = c_i
            if l <= res <= r and (_max - _min) >= x:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main(10)