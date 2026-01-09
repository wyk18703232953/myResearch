def main(n):
    # Deterministic data generation:
    # Map n to N and M, and construct L similar to an increasing sequence.
    if n <= 0:
        return
    N = n
    M = 3 * n + 5
    # Generate N integers strictly increasing and within (0, M)
    # Example: L[i] = i * 2, ensuring L[N] < M for n reasonably small vs M
    L = [0] + [2 * i for i in range(1, N + 1)] + [M]
    sumL = [0]
    ans = -10**30
    for i in range(1, N + 1):
        sumL.append(sumL[-1] - (-1) ** i * L[i])
    for i in range(1, N + 1):
        if L[i] > L[i - 1] + 1:
            ans = max(ans, 2 * sumL[i - 1] - sumL[-1] - (-1) ** i * (L[i] - 1))
        if L[i] < L[i + 1] - 1:
            ans = max(ans, 2 * sumL[i] - sumL[-1] + (-1) ** i * (L[i] + 1))
    if N % 2 == 0:
        result = max(ans, sumL[-1] + M)

    else:
        result = max(ans + M, sumL[-1])
    # print(result)
    pass
if __name__ == "__main__":
    main(10)