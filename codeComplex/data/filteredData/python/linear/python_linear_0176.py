def main(n):
    # Interpret n as the number of elements; also derive k deterministically
    # Ensure k is at least 1 and at most n
    if n <= 0:
        return
    k = max(1, n // 3)
    if k > n:
        k = n

    # Deterministic generation of theorems and sleep arrays
    theorems = [(i * 7 + 3) % 100 for i in range(n)]
    sleep = [1 if i % 2 == 0 else 0 for i in range(n)]

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

    # print(slsum + maxdiff)
    pass
if __name__ == "__main__":
    main(10)