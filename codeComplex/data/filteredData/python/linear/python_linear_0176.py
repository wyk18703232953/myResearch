def main(n):
    # Interpret n as the length of the theorem list and sleep list
    if n <= 0:
        print(0)
        return

    # Choose k deterministically based on n, with 1 <= k <= n
    # For example: k = max(1, n // 2)
    k = n // 2
    if k == 0:
        k = 1

    # Deterministic generation of theorems and sleep arrays
    # theorems[i] = (i * 3 + 1) % 100 + 1  (values in [1, 100])
    theorems = [((i * 3 + 1) % 100) + 1 for i in range(n)]
    # sleep[i] = i % 2  (alternating 0,1,0,1,...)
    sleep = [i % 2 for i in range(n)]

    tsum = []
    ts = 0
    sleepsum = []
    slsum = 0
    for i in range(n):
        ts += theorems[i]
        tsum.append(ts)
        if sleep[i] == 1:
            slsum += theorems[i]
        sleepsum.append(slsum)

    maxdiff = tsum[k - 1] - sleepsum[k - 1]
    for i in range(1, n - k + 1):
        diff = (tsum[i + k - 1] - tsum[i - 1]) - (sleepsum[i + k - 1] - sleepsum[i - 1])
        if diff > maxdiff:
            maxdiff = diff

    print(slsum + maxdiff)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)