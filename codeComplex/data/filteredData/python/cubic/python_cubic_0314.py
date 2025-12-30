import random

def main(n):
    # 1. 根据规模 n 生成数据
    # 这里将 r, g, b 都设置为 n，并生成对应长度的随机正整数
    r = g = b = n
    R = [random.randint(1, 1000) for _ in range(r)]
    G = [random.randint(1, 1000) for _ in range(g)]
    B = [random.randint(1, 1000) for _ in range(b)]

    # 保持与原代码一致的逻辑：排序
    R.sort()
    G.sort()
    B.sort()

    # 初始化 dp 数组
    dp = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    def solve(rr, gg, bb):
        if ((rr == 0 and gg == 0) or
            (gg == 0 and bb == 0) or
            (bb == 0 and rr == 0)):
            return 0
        if dp[rr][gg][bb] == -1:
            if rr == 0:
                ans = G[gg - 1] * B[bb - 1] + solve(rr, gg - 1, bb - 1)
            elif gg == 0:
                ans = R[rr - 1] * B[bb - 1] + solve(rr - 1, gg, bb - 1)
            elif bb == 0:
                ans = G[gg - 1] * R[rr - 1] + solve(rr - 1, gg - 1, bb)
            else:
                ans = max(
                    G[gg - 1] * B[bb - 1] + solve(rr,     gg - 1, bb - 1),
                    G[gg - 1] * R[rr - 1] + solve(rr - 1, gg - 1, bb    ),
                    R[rr - 1] * B[bb - 1] + solve(rr - 1, gg,     bb - 1)
                )
            dp[rr][gg][bb] = ans
        return dp[rr][gg][bb]

    ans = solve(r, g, b)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，设定规模 n
    main(5)