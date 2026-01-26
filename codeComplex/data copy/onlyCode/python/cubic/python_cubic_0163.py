from sys import stdin, gettrace

if not gettrace():
    def input():
        return next(stdin)[:-1]


# def input():
#    return stdin.buffer.readline()

INF = 10000


def main():
    n = int(input())
    aa = [int(a) for a in input().split()]

    dp = [[0] * (n+1) for _ in range(n)]

    def calc_dp(i, j):
        if i + 1 == j:
            dp[i][j] = aa[i]
        if dp[i][j] != 0:
            return dp[i][j]
        dp[i][j] = -1
        for k in range(i+1, j):
            lf = calc_dp(i, k)
            rg = calc_dp(k, j)
            if lf > 0 and lf == rg:
                dp[i][j] = lf + 1
                break
        return dp[i][j]

    dp2 = list(range(0,n+1))
    for i in range(n):
        for j in range(i+1, n+1):
            if calc_dp(i, j) > 0:
                dp2[j] = min(dp2[j], dp2[i] + 1)
    print(dp2[n])





if __name__ == "__main__":
    main()