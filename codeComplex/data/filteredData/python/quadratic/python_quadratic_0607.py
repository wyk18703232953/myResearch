def main(n):
    # Interpret n as N (array length); fix M and K as simple functions of n
    if n <= 0:
        # print(0)
        pass
        return

    N = n
    M = max(1, n // 3)  # number of residue classes
    K = (n % 5) + 1     # penalty

    # Deterministic array of length N
    arr = [(i * 2 + (i // 3)) % (n + 7) for i in range(N)]

    res = 0
    for j in range(M):
        s = 0
        mini = 0
        for i in range(j, N):
            if i % M == j:
                mini = min(mini, s)
                s -= K
            s += arr[i]
            if s - mini > res:
                res = s - mini
    # print(res)
    pass
if __name__ == "__main__":
    main(1000)