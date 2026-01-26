r, g, b = map(int, input().split())
R = list(map(int, input().split()))
G = list(map(int, input().split()))
B = list(map(int, input().split()))
R.sort(reverse=True)
G.sort(reverse=True)
B.sort(reverse=True)

memo = [[[-1]*(b+1) for i in range(g+1)] for j in range(r+1)]

def calc(ir, ig, ib):
    if memo[ir][ig][ib] != -1:
        return memo[ir][ig][ib]
    ans = 0
    if ir < r and ig < g:
        ans = max(ans, calc(ir+1, ig+1, ib)+R[ir]*G[ig])
    if ir < r and ib < b:
        ans = max(ans, calc(ir+1, ig, ib+1)+R[ir]*B[ib])
    if ig < g and ib < b:
        ans = max(ans, calc(ir, ig+1, ib+1)+G[ig]*B[ib])
    memo[ir][ig][ib] = ans
    return ans

print(calc(0, 0, 0))
