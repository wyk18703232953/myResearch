def main(n):
    # Interpret n as the length of arr
    # Deterministically generate k and arr
    if n <= 0:
        return

    # Choose k deterministically based on n, ensure 1 <= k <= min(n, some upper bound)
    # For complexity experiments, let k vary with n but remain valid.
    k = max(1, min(n, n // 3 if n >= 3 else 1))

    # Generate arr with values in a bounded range [1, max_val]
    max_val = 10**5
    # Use a simple deterministic pattern; wrap values into [1, max_val]
    arr = [((i * 7 + 3) % max_val) + 1 for i in range(n)]

    count = [0] * (max_val + 1)

    for v in arr:
        count[v] += 1

    s = sum(1 for c in count if c > 0)
    if s < k:
        # print('-1 -1')
        pass
        return

    r = n - 1
    while True:
        if count[arr[r]] == 1:
            s -= 1
            if s < k:
                s += 1
                break
        count[arr[r]] -= 1
        r -= 1

    l = 0
    while True:
        if count[arr[l]] == 1:
            s -= 1
            if s < k:
                s += 1
                break
        count[arr[l]] -= 1
        l += 1

    # print(l + 1, r + 1)
    pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10**5)