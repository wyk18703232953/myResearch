
R,G,B=[int(c) for c in input().split()]
ra=[int(c) for c in input().split()]
ga=[int(c) for c in input().split()]
ba=[int(c) for c in input().split()]

ra.sort(reverse=True)
ga.sort(reverse=True)
ba.sort(reverse=True)

dp = [[[-1 for i in range(201)]for j in range(201)]for k in range(201)]
def solve(dp,r,g,b):
    if dp[r][g][b] !=-1:
        return dp[r][g][b]
    count= 0
    for i,j in zip((r,g,b),(R,G,B)):
        if i == j:
            count+=1
    if count >= 2:
        return 0

    ##Three cases choose btw r,b r,g  and gb
    res = -999
    if r != R and b!=B:

        res = max(res,ra[r]*ba[b] + solve(dp,r+1,g,b+1))
        # print(res)
    
    if r!=R and g != G:
        res = max(res,ra[r]*ga[g] + solve(dp,r+1,g+1,b))
        # print(res)
    
    if b!=B and g != G:
        res = max(res,ba[b]*ga[g] + solve(dp,r,g+1,b+1))
        # print(res)
    
    dp[r][g][b] = res

    return res
     

print(solve(dp,0,0,0))