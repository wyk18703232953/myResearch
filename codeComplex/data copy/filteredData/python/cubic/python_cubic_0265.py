def solve(i, j, k, R, G, B, dp):
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    call = 0
    if i > 0 and j > 0:
        call = max(call, R[i] * G[j] + solve(i - 1, j - 1, k, R, G, B, dp))
    if j > 0 and k > 0:
        call = max(call, G[j] * B[k] + solve(i, j - 1, k - 1, R, G, B, dp))
    if k > 0 and i > 0:
        call = max(call, B[k] * R[i] + solve(i - 1, j, k - 1, R, G, B, dp))
    dp[i][j][k] = call
    return call


def main(n):
    if n < 1:
        n = 1
    nr = n
    ng = n
    nb = n

    R = [0] + [i for i in range(1, nr + 1)]
    G = [0] + [i * 2 for i in range(1, ng + 1)]
    B = [0] + [i * 3 for i in range(1, nb + 1)]

    R.sort()
    G.sort()
    B.sort()

    dp = [[[-1] * (nb + 1) for _ in range(ng + 1)] for _ in range(nr + 1)]
    ans = solve(nr, ng, nb, R, G, B, dp)
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)