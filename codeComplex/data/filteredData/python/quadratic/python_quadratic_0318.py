def main(n):
    # n controls both the array size and the upper bound for k
    if n <= 0:
        # print(0.0)
        pass
        return

    # Deterministic generation of n and k
    # Let the original n be N, and k be about N//3 at minimum 1
    N = n
    k = max(1, N // 3)

    # Deterministic array: arr[i] = (i * 7) % 100 - 50  (values in [-50,49])
    arr = [((i * 7) % 100) - 50 for i in range(N)]

    rsum = [0]
    maxx = 0.0

    for i in range(N):
        rsum.append(rsum[-1] + arr[i])

    for ki in range(k, N + 1):
        for i in range(N - ki + 1):
            avg = (rsum[i + ki] - rsum[i]) / ki
            if avg > maxx:
                maxx = avg

    # print(maxx)
    pass
if __name__ == "__main__":
    main(1000)