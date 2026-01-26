def main(n):
    # n: number of points (original input size)
    if n <= 0:
        return 0

    # Deterministic generation of d and array a based on n
    d = n // 3 + 1  # step distance
    a = [i * d for i in range(n)]  # strictly increasing positions

    pos = 2
    for i in range(n - 1):
        l = a[i] + d
        r = a[i + 1] - d
        if l == r:
            pos += 1
        elif l < r:
            pos += 2
    return pos


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    result = main(10)
    # print(result)
    pass