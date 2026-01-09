def main(n):
    # Map n to problem parameters:
    # n = length of p, k = max segment length (bounded by 256)
    if n <= 0:
        return
    k = max(1, min(256, n // 2 + 1))

    # Deterministic generation of p: cycle through [0..255]
    p = [i % 256 for i in range(n)]

    choosed = [False] * 256
    left = [i for i in range(256)]

    for i, x in enumerate(p):
        if not choosed[x]:
            best = x
            for j in range(x - 1, max(-1, x - k), -1):
                if not choosed[j]:
                    best = j

                else:
                    if x - left[j] < k:
                        best = left[j]
                    break
            for j in range(best, x + 1):
                choosed[j] = True
                left[j] = best
        p[i] = left[x]

    # print(' '.join(map(str, p)))
    pass
if __name__ == "__main__":
    # Example scale; adjust as needed for experiments
    main(1000)