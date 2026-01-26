#tests = int(input())
#for t in range(tests):
#    b= int(input())
#    ls = [int(x) for x in input()]

r,g,b = list(map(int, input().split()))
ls_r = sorted(list(map(int, input().split())))
ls_g = sorted(list(map(int, input().split())))
ls_b = sorted(list(map(int, input().split())))


dp = [[[-1 for _ in range(b+1)]for _ in range(g+1)]for _ in range(r+1)]

def recursive(idx_r, idx_g, idx_b):
    if dp[idx_r][idx_g][idx_b] != -1:
        return dp[idx_r][idx_g][idx_b]
    res_1 = 0
    res_2 = 0
    res_3 = 0
    if (idx_r-1) >= 0 and (idx_g-1) >= 0:
        res_1 = recursive(idx_r-1, idx_g-1, idx_b) + ls_r[idx_r-1] * ls_g[idx_g-1]
    if (idx_g-1) >= 0 and (idx_b-1) >= 0:
        res_2 = recursive(idx_r, idx_g-1, idx_b-1) + ls_g[idx_g-1] * ls_b[idx_b-1]
    if (idx_r-1) >= 0 and (idx_b-1) >= 0:
        res_3 = recursive(idx_r-1, idx_g, idx_b-1) + ls_r[idx_r-1] * ls_b[idx_b-1]
    
    dp[idx_r][idx_g][idx_b] = max(res_1, res_2, res_3)
    return dp[idx_r][idx_g][idx_b]

print(recursive(r,g,b))