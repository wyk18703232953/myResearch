import sys

def dp(ri, gi, bi):
    if ri>r or gi>g or bi>b:
        return 0

    if not list_memo[ri][gi][bi]==-1:
        return list_memo[ri][gi][bi]
    
    list_memo[ri][gi][bi] = max(dp(ri+1, gi+1, bi)+r_c[ri]*g_c[gi], dp(ri+1, gi, bi+1)+r_c[ri]*b_c[bi], dp(ri, gi+1, bi+1)+g_c[gi]*b_c[bi])
    return list_memo[ri][gi][bi]


r, g, b = map(int, sys.stdin.readline().split())

r_c = sorted(list(map(int, sys.stdin.readline().split()))+[0], reverse=1)
g_c = sorted(list(map(int, sys.stdin.readline().split()))+[0], reverse=1)
b_c = sorted(list(map(int, sys.stdin.readline().split()))+[0], reverse=1)


list_memo = [[[-1]*(b+1) for _ in range(g+1)] for _ in range(r+1)]

print(dp(0, 0, 0))