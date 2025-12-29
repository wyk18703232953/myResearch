from array import array
import random

def recSolve(dp, r, g, b, rx, gx, bx, R, G, B):
    if rx == R:
        return sum(a * b for a, b in zip(g[gx:], b[bx:]))
    if gx == G:
        return sum(a * b for a, b in zip(r[rx:], b[bx:]))
    if bx == B:
        return sum(a * b for a, b in zip(g[gx:], r[rx:]))

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
    # 根据规模 n 生成 R, G, B（尽量均分）
    R = n // 3
    G = (n - R) // 2
    B = n - R - G
    if R == 0: R = 1
    if G == 0: G = 1
    if B == 0: B = 1

    # 生成测试数据：1 到 100 的随机整数
    random.seed(0)
    r = sorted([random.randint(1, 100) for _ in range(R)], reverse=True)
    g = sorted([random.randint(1, 100) for _ in range(G)], reverse=True)
    b = sorted([random.randint(1, 100) for _ in range(B)], reverse=True)

    dp = array('q', (-1 for _ in range(R * G * B)))
    ans = recSolve(dp, r, g, b, 0, 0, 0, R, G, B)
    print(ans)

if __name__ == "__main__":
    # 示例：n = 9
    main(9)