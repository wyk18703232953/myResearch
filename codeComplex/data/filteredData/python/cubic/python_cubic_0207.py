import random

def main(n):
    # 规模 n 用来控制 R, G, B 的大小，这里简单设为都等于 n
    R = G = B = n

    # 生成测试数据：随机正整数（可以按需调整范围）
    r = [random.randint(1, 1000) for _ in range(R)]
    g = [random.randint(1, 1000) for _ in range(G)]
    b = [random.randint(1, 1000) for _ in range(B)]

    # 原逻辑
    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    dp = [[[-1] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]

    def calc(nr, ng, nb):
        if dp[nr][ng][nb] != -1:
            return dp[nr][ng][nb]
        res = 0
        if nr < R and ng < G:
            res = max(res, calc(nr + 1, ng + 1, nb) + r[nr] * g[ng])
        if nr < R and nb < B:
            res = max(res, calc(nr + 1, ng, nb + 1) + r[nr] * b[nb])
        if ng < G and nb < B:
            res = max(res, calc(nr, ng + 1, nb + 1) + g[ng] * b[nb])
        dp[nr][ng][nb] = res
        return res

    ans = calc(0, 0, 0)
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：n=3
    main(3)