def main(n):
    # n: number of intervals
    # We also need a deterministic t
    # Define t as a simple function of n to scale with input
    t = n // 3 + 1

    arr = []
    # Deterministically generate (a, b) pairs
    # Ensure b > 0 to make intervals meaningful
    for i in range(n):
        a = i * 2
        b = (i % 5) + 1
        arr.append((a - (b / 2), a + (b / 2)))

    arr.sort()
    ans = 0
    for i in range(1, n):
        diff = abs(arr[i][0] - arr[i - 1][1])
        if diff == t:
            ans += 1
        elif diff > t:
            ans += 2

    result = ans + 2
    print(result)
    return result


if __name__ == "__main__":
    main(10)