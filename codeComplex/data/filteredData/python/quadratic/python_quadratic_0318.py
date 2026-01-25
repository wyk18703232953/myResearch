def main(n):
    # Interpret n as both array length and upper bound of k
    # To keep structure similar to original: choose k = max(1, n // 2)
    if n <= 0:
        return 0.0

    k = max(1, n // 2)

    # Deterministic data generation based on n
    # Example: arr[i] = (i * 3 + 1) % (n + 5) + 1
    arr = [((i * 3 + 1) % (n + 5)) + 1 for i in range(n)]

    rsum = [0]
    maxx = 0.0

    for i in range(n):
        rsum.append(rsum[-1] + arr[i])

    # In original code, k is an upper bound for subarray length
    for ki in range(k, n + 1):
        for i in range(n - ki + 1):
            avg = (rsum[i + ki] - rsum[i]) / ki
            if avg > maxx:
                maxx = avg

    return maxx


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    result = main(10)
    print(result)