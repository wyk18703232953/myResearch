T = int(input())
for ti in range(T):
    s = input().strip()
    t = input().strip()
    N = len(t)
    for i in range(1, N+1):
        # t1 : [0,i), t2 : [i,N)に分割
        dp = [[0]+[-1]*i for _ in range(len(s)+1)]
        for l, c in enumerate(s):
            for j in range(i+1):
                dp[l+1][j] = dp[l][j]
                # t1[0:j]を構成した時にt2はどこまで構成できるか
                # cをt2に使う
                if dp[l][j] != -1:
                    if i+dp[l][j] < N and t[i+dp[l][j]] == c:
                        dp[l+1][j] = dp[l][j]+1
#                    print(l+1, i+dp[l][j], c, t[i+dp[l][j+1]])
                # cをt1に使う
                if j != 0 and c == t[j-1]:
                    dp[l+1][j] = max(dp[l+1][j], dp[l][j-1])
#                    print(l+1, j+1, dp[l][j])
#        print(ti, i, dp, dp[-1][i])
        if dp[-1][i] == N-i:
            print("YES")
            break
    else:
        print("NO")

