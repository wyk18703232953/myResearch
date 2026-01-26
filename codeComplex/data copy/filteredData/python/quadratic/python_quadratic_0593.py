def main(n):
    # Interpret n as N; fix M,K to reasonable deterministic values
    N = max(1, n)
    M = 10
    K = 5

    # Deterministically generate A of length N
    # Example pattern: A[i] = (i * 7 + 3) % 100 + 1
    A = [((i * 7 + 3) % 100) + 1 for i in range(N)]

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
    main(1000)