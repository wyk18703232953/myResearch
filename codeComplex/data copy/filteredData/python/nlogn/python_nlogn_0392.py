def main(n):
    # Interpret n as the length of arrays p and c, and also k
    if n <= 0:
        return

    # Deterministically generate p and c based on n
    # p: increasing-ish but with some structure, c: positive values
    p = [(i * 3 + 7) % (2 * n + 1) + 1 for i in range(n)]
    c = [(i * 5 + 11) % (3 * n + 1) + 1 for i in range(n)]
    k = n

    from heapq import heappop, heappush, heapify

    arr = [i for i in sorted(enumerate(p), key=lambda x: x[1])]
    maxcoins = [0 for _ in range(k)]
    heapify(maxcoins)
    ans = list(p)
    tmpSum = 0
    tmpSum2 = 0
    prev = arr[0][1]
    for ind, power in arr:
        if power > prev:
            ans[ind] = tmpSum + c[ind]
            tmpSum2 = tmpSum

        else:
            ans[ind] = tmpSum2 + c[ind]
        heappush(maxcoins, c[ind])
        tmpSum += c[ind]
        tmpSum -= heappop(maxcoins)
        prev = power
    # print(*ans)
    pass
if __name__ == "__main__":
    main(10)