def rec(r, g, b, R, G, B, red, green, blue, dp):
    if dp[r][g][b] != -1:
        return dp[r][g][b]
    ans = 0
    if r < R and g < G:
        ans = max(ans, red[r] * green[g] + rec(r + 1, g + 1, b, R, G, B, red, green, blue, dp))
    if r < R and b < B:
        ans = max(ans, red[r] * blue[b] + rec(r + 1, g, b + 1, R, G, B, red, green, blue, dp))
    if b < B and g < G:
        ans = max(ans, blue[b] * green[g] + rec(r, g + 1, b + 1, R, G, B, red, green, blue, dp))
    dp[r][g][b] = ans
    return ans

def generate_data(n):
    # 映射规则：
    # R, G, B 为同一规模 n
    # 列表内容为确定性的整数序列，与 n 相关
    R = n
    G = n
    B = n
    red = [i * 2 + 1 for i in range(R)]
    green = [i * 3 + 2 for i in range(G)]
    blue = [i * 5 + 3 for i in range(B)]
    red.sort(reverse=True)
    green.sort(reverse=True)
    blue.sort(reverse=True)
    return R, G, B, red, green, blue

def main(n):
    R, G, B, red, green, blue = generate_data(n)
    dp = [[[-1] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]
    result = rec(0, 0, 0, R, G, B, red, green, blue, dp)
    # print(result)
    pass
if __name__ == "__main__":
    main(3)