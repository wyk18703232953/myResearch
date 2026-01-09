import math

def main(n):
    # Ensure n is at least 1
    if n <= 0:
        return

    # Deterministically generate input array A of length n
    # Example pattern: A[i] cycles through 1..5 based on index
    A = [(i % 5) + 1 for i in range(n)]

    inf = float("inf")
    DP = [[inf] * (n + 1) for _ in range(n + 1)]

    for j in range(1, n + 1):
        for i in range(n):
            if i + j > n:
                continue

            else:
                if j == 1:
                    DP[i][i + 1] = A[i]

                else:
                    for k in range(i + 1, i + j):
                        if DP[i][k] < 10000 and DP[k][i + j] < 10000:
                            if DP[i][k] == DP[k][i + j]:
                                DP[i][i + j] = DP[i][k] + 1

                            else:
                                DP[i][i + j] = 20000

                        else:
                            if DP[i][k] < 10000:
                                DP[i][i + j] = min(DP[i][i + j], 10000 + DP[k][i + j])
                            elif DP[k][i + j] < 10000:
                                DP[i][i + j] = min(DP[i][i + j], DP[i][k] + 10000)

                            else:
                                DP[i][i + j] = min(DP[i][i + j], DP[i][k] + DP[k][i + j])

    result = DP[0][n] // 10000 if DP[0][n] >= 10000 else 1
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call for experimental purpose
    main(10)