def main(n):
    # Interpret n as the size of the original array
    # Choose k deterministically as a function of n, ensuring 1 <= k <= n
    if n <= 0:
        return
    k = max(1, n // 3)
    if k > n:
        k = n

    # Deterministic construction of arr with n elements
    # Example: strictly increasing sequence to keep differences positive
    arr = [i * 2 + (i // 2) for i in range(n)]

    new_arr = []
    for i in range(n - 1):
        new_arr.append(arr[i + 1] - arr[i])

    new_arr.sort()
    # Ensure we don't slice with negative size when k > n (already handled, but be safe)
    limit = max(0, n - k)
    result = sum(new_arr[:limit])
    print(result)


if __name__ == "__main__":
    main(10)