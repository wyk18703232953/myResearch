from array import array

def recSolve(dp, r, g, b, rx, gx, bx, R, G, B):
    if rx == R:
        return sum(a * c for a, c in zip(g[gx:], b[bx:]))
    if gx == G:
        return sum(a * c for a, c in zip(r[rx:], b[bx:]))
    if bx == B:
        return sum(a * c for a, c in zip(g[gx:], r[rx:]))
    idx = rx * G * B + gx * B + bx
    if dp[idx] != -1:
        return dp[idx]
    rg = recSolve(dp, r, g, b, rx + 1, gx + 1, bx, R, G, B) + r[rx] * g[gx]
    bg = recSolve(dp, r, g, b, rx, gx + 1, bx + 1, R, G, B) + b[bx] * g[gx]
    rb = recSolve(dp, r, g, b, rx + 1, gx, bx + 1, R, G, B) + r[rx] * b[bx]
    ans = max(rg, bg, rb)
    dp[idx] = ans
    return ans

def main(n):
    if n <= 0:
        return 0
    # 映射规模：R = G = B = n
    R = G = B = n
    # 确定性构造原本会被排序为降序的数组
    r = [n * 3 - i for i in range(1, R + 1)]
    g = [n * 2 - i for i in range(1, G + 1)]
    b = [n - i for i in range(1, B + 1)]
    dp = array('q', (-1 for _ in range(R * G * B)))
    return recSolve(dp, r, g, b, 0, 0, 0, R, G, B)

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    result = main(3)
    # print(result)
    pass