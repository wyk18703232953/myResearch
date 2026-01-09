def cal(r, g, b, R, G, B, rl, gl, bl, dp):
    if dp[r][g][b] != -1:
        return dp[r][g][b]
    ans = 0
    if r < R and g < G:
        ans = max(ans, rl[r] * gl[g] + cal(r + 1, g + 1, b, R, G, B, rl, gl, bl, dp))
    if r < R and b < B:
        ans = max(ans, rl[r] * bl[b] + cal(r + 1, g, b + 1, R, G, B, rl, gl, bl, dp))
    if g < G and b < B:
        ans = max(ans, gl[g] * bl[b] + cal(r, g + 1, b + 1, R, G, B, rl, gl, bl, dp))
    dp[r][g][b] = ans
    return ans

def main(n):
    R = n
    G = n
    B = n
    rl = sorted([i + 1 for i in range(R)], reverse=True)
    gl = sorted([2 * (i + 1) for i in range(G)], reverse=True)
    bl = sorted([3 * (i + 1) for i in range(B)], reverse=True)
    dp = [[[-1 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]
    result = cal(0, 0, 0, R, G, B, rl, gl, bl, dp)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)