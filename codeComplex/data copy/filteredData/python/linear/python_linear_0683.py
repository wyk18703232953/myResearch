def main(n):
    # Ensure n is at least 2 to avoid invalid indexing; adjust if smaller
    if n < 2:
        n = 2

    # Generate deterministic input b based on n
    # b has length n and all elements are positive
    b = [i * 2 + 1 for i in range(n)]

    a = [0] * n

    minV = 0
    maxV = b[0]

    m = n // 2

    a[n - 1] = b[0]

    i = 1
    j = n - 2

    while i < m:
        if b[i] - minV > 0 and b[i] - minV <= maxV:
            a[i] = minV
            a[j] = b[i] - minV
            maxV = min(maxV, b[i] - minV)

        else:
            a[i] = b[i] - maxV
            a[j] = maxV
            minV = max(minV, b[i] - maxV)

        i += 1
        j -= 1

    # print(' '.join(map(str, a)))
    pass
if __name__ == "__main__":
    main(10)