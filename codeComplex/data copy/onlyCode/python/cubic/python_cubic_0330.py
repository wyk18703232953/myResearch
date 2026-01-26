from collections import defaultdict


def main():
    R, G, B = map(int, input().split())
    red = list(map(int, input().split()))
    green = list(map(int, input().split()))
    blue = list(map(int, input().split()))
    red.sort(reverse=True)
    green.sort(reverse=True)
    blue.sort(reverse=True)
    dp = [[[-2*10**9]*(B+10) for i in range(G+10)] for j in range(R+10)]
    dp[0][0][0] = 0
    ans = 0
    for i in range(R+1):
        for j in range(G+1):
            for k in range(B+1):
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k]+red[i-1]*green[j-1], dp[i]
                                  [j-1][k-1]+green[j-1]*blue[k-1], dp[i-1][j][k-1]+red[i-1]*blue[k-1])
                ans = max(ans, dp[i][j][k])
    print(ans)
    return


if __name__ == "__main__":
    main()


