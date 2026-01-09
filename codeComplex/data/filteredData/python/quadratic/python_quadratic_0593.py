def main(n):
    # Interpret n as N and M simultaneously for scalability
    N = n
    M = max(1, n)  # ensure M >= 1
    # Define K deterministically based on n
    K = n // 2 + 1

    # Generate A as a deterministic list of length N
    # Example pattern: A[i] = (i % (2*M + 1)) - M  (can be negative and positive)
    A = [((i % (2 * M + 1)) - M) for i in range(N)]

    S = [0]
    for a in A:
        S.append(S[-1] + M * a - K)

    MI = [(10**50)] * M
    ans = 0
    for i in range(N + 1):
        MI[i % M] = min(MI[i % M], S[i])
        for j in range(M):
            ans = max(ans, (S[i] - MI[(i - j) % M] - K * ((-j) % M)) // M)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)