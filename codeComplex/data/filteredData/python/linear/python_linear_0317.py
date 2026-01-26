def main(n):
    # Map n to problem scale.
    # We create:
    #   m = max(1, n // 3)
    #   array length = n
    #   arr[i] = (i * 7 + 3) % (2 * m + 1)  (deterministic, depends on n)
    if n < 1:
        return

    m = max(1, n // 3)

    # Generate deterministic input data
    arr = [(i * 7 + 3) % (2 * m + 1) for i in range(n)]
    s = sum(arr)

    idx = [[] for _ in range(m)]
    for i in range(n):
        idx[arr[i] % m].append(i)

    j = 0
    for i in range(m):
        while len(idx[i]) > n // m:
            while True:
                if j < i:
                    j += 1
                elif len(idx[j % m]) >= n // m:
                    j += 1

                else:
                    break
            last = idx[i].pop()
            arr[last] += (j - i) % m
            idx[j % m].append(last)

    # Match original outputs: first the total increment, then final array
    # print(sum(arr) - s)
    pass
    # print(*arr)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale the experiment
    main(10)