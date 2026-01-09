def main(n):
    # n is the length of the array
    if n <= 0:
        return "NO"
    # Deterministic data generation:
    # Create an array that increases then decreases with a single peak
    # Example pattern: [0, 1, 2, ..., n//2, n//2 - 1, ..., 1] (length n, adjusted)
    peak = n // 2
    inc_part = list(range(peak + 1))
    dec_length = n - len(inc_part)
    dec_part = list(range(peak - 1, peak - 1 - dec_length, -1)) if dec_length > 0 else []
    a = inc_part + dec_part

    # Original logic
    i = a.index(max(a))
    v = True
    for j in range(0, i):
        if a[j] > a[j + 1]:
            v = False
    for j in range(i, n - 1):
        if a[j] < a[j + 1]:
            v = False
    return "YES" if v else "NO"


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    result = main(10)
    # print(result)
    pass