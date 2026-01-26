def main(n):
    # n: length of array; k is derived deterministically from n
    if n <= 0:
        return

    # Deterministically choose k based on n, but at least 1
    k = max(1, n // 3)

    # Generate deterministic array values in range [1, 100000]
    # Keep values small enough for the count array
    MOD = 100000
    arr = [((i * 37 + 13) % MOD) + 1 for i in range(n)]

    count = [0] * (MOD + 1)

    for x in arr:
        count[x] += 1

    s = sum(1 for c in count if c > 0)
    if s < k:
        # print("-1 -1")
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
    # Example deterministic call
    main(1000)