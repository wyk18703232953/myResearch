def main(n):
    # Interpret n as N (array length)
    # Choose M and K deterministically based on n
    if n <= 0:
        # print(0)
        pass
        return

    N = n
    M = max(1, n // 3)  # ensure 1 <= M <= N
    K = (n // 2) + 1

    # Deterministic construction of arr with length N
    # Example pattern: arr[i] = (i % 7) - 3
    arr = [(i % 7) - 3 for i in range(N)]

    res = 0
    for j in range(M):
        s = 0
        mini = 0
        for i in range(j, N):
            if i % M == j:
                mini = min(mini, s)
                s -= K
            s += arr[i]
            res = max(res, s - mini)

    # print(res)
    pass
if __name__ == "__main__":
    main(10)