r,g,b = map(int,input().split())
rs = list(map(int,input().split()))
gs = list(map(int,input().split()))
bs = list(map(int,input().split()))
rs.sort()
gs.sort()
bs.sort()
rs.reverse()
gs.reverse()
bs.reverse()
dp = [[[0]*201 for x in range(201)] for y in range(201)]
for i in range(min(r,g)+1):
    for j in range(min(g,b)+1):
        for k in range(min(b,r)+1):
            options = []
##            if i == 0 and j == 0:
##                dp[i][j][k] = dp[i][j][k-1] + bs[k-1]*rs[k-1]
##                continue
##            elif j == 0 and k == 0:
##                dp[i][j][k] = dp[i-1][j][k] + rs[i-1]*gs[i-1]
##                continue
##            elif i == 0 and k == 0:
##                dp[i][j][k] = dp[i][j-1][k] + gs[j-1]*bs[j-1]
##                continue
            if i == 0:
                pass
            elif i+k-1 < r and i+j-1 < g:
                options.append(dp[i-1][j][k] + rs[i+k-1]*gs[i+j-1])
            else:
                options.append(dp[i-1][j][k])
            if j == 0:
                pass
            elif i+j-1 < g and j+k-1 < b:
                options.append(dp[i][j-1][k] + gs[i+j-1]*bs[j+k-1])
            else:
                options.append(dp[i][j-1][k])
            if k == 0:
                pass
            elif j+k-1 < b and i+k-1 < r:
                options.append(dp[i][j][k-1] + bs[j+k-1]*rs[i+k-1])
            else:
                options.append(dp[i][j][k-1])
            if len(options) == 0:
                continue
            dp[i][j][k] = max(options)
print(dp[min(r,g)][min(g,b)][min(r,b)])           


##rp = r-1
##gp = g-1
##bp = b-1
##ans = 0
##m = min(rs[rp],gs[gp],bs[bp])
##if m == rs[rp] and m == gs[gp]:
##    if rp < gp:
##        ans += bs[bp]*gs[gp]
