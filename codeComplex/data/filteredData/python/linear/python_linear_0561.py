def main(n):
    # Deterministic generation of k and the array based on n
    # Map n to:
    #   - length of array = n
    #   - k chosen as a small function of n but bounded to keep (1 << k) reasonable
    if n <= 0:
        # print(0)
        pass
        return

    k = (n % 20) + 1  # k in [1, 20]
    max_val = (1 << k) - 1

    # Generate a deterministic array of length n with values in [0, max_val]
    arr = [((i * 17 + 23) ^ (i // 3)) & max_val for i in range(n)]

    d = {0: 1}
    x = 0
    for val in arr:
        x ^= val
        v = min(x, (1 << k) - x - 1)
        if v not in d:
            d[v] = 0
        d[v] += 1

    ans = 0
    for _, v in d.items():
        c1 = v // 2
        c2 = v - c1
        ans += c1 * (c1 - 1) // 2 + c2 * (c2 - 1) // 2

    # print(n * (n - 1) // 2 + n - ans)
    pass
if __name__ == "__main__":
    main(10)