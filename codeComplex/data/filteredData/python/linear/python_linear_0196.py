def main(n):
    # Deterministically generate inputs based on n
    # Map n to:
    #   - number of elements: n
    #   - T: upper limit for the outer loop and count target
    #   - a, b, c: some deterministic functions of n
    a = n + 1
    b = (n // 2) + 1
    c = (n % 5) + 1
    T = max(1, n // 3)

    # Ensure array values are within a reasonable range around T
    # Deterministic pattern using simple arithmetic
    arr = [(i % (T + 1)) for i in range(n)]

    # Original core logic
    Tcnt = arr.count(T)
    l = n - Tcnt  # unused but kept to preserve structure
    ans = 0
    a1 = 0

    for i in range(1, T):
        for j in range(n):
            if arr[j] <= i:
                a1 += 1
        ans += a1 * c
        a1 = 0

    b1 = 0
    for i in range(n):
        b1 = a - ((T - arr[i]) * b)
        if b1 <= 0:
            ans += b1

        else:
            ans += b1

    ans1 = n * a
    result = max(ans, ans1)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example call for time complexity experiments
    main(1000)