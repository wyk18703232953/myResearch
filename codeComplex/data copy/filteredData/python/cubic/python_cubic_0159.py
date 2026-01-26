from collections import defaultdict

def main(n):
    N = n
    if N <= 0:
        # print(0)
        pass
        return
    X = [i % 5 for i in range(N)]
    dp1 = defaultdict(lambda: -1)
    M = N + 2
    def ec(i, j):
        return i * M + j

    for i in range(N):
        dp1[ec(i, i + 1)] = X[i]
    for length in range(2, N + 1):
        for j in range(N - length + 1):
            for k in range(1, length):
                u = dp1[ec(j, j + k)]
                v = dp1[ec(j + k, j + length)]
                if u != -1 and v != -1 and u == v:
                    dp1[ec(j, j + length)] = u + 1
                    break

    dp2 = [10 ** 18] * (N + 1)
    dp2[0] = 0
    for i in range(N):
        for j in range(i + 1):
            if dp1[ec(j, i + 1)] == -1:
                continue
            if dp2[j] + 1 < dp2[i + 1]:
                dp2[i + 1] = dp2[j] + 1
    # print(dp2[-1])
    pass
if __name__ == "__main__":
    main(10)