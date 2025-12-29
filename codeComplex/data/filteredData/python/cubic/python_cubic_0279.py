import random

def solve(r, g, b, rs, gs, bs):
    rs.sort(reverse=True)
    gs.sort(reverse=True)
    bs.sort(reverse=True)
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]
    sol = 0
    for ri in range(r + 1):
        for gi in range(g + 1):
            for bi in range(b + 1):
                if ri < r and gi < g:
                    dp[ri + 1][gi + 1][bi] = max(
                        dp[ri + 1][gi + 1][bi],
                        rs[ri] * gs[gi] + dp[ri][gi][bi]
                    )
                if ri < r and bi < b:
                    dp[ri + 1][gi][bi + 1] = max(
                        dp[ri + 1][gi][bi + 1],
                        rs[ri] * bs[bi] + dp[ri][gi][bi]
                    )
                if gi < g and bi < b:
                    dp[ri][gi + 1][bi + 1] = max(
                        dp[ri][gi + 1][bi + 1],
                        gs[gi] * bs[bi] + dp[ri][gi][bi]
                    )
                sol = max(sol, dp[ri][gi][bi])
    return sol

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单设定 r, g, b 各为 n，元素值在 [1, 100] 区间随机生成
    r = g = b = n
    rs = [random.randint(1, 100) for _ in range(r)]
    gs = [random.randint(1, 100) for _ in range(g)]
    bs = [random.randint(1, 100) for _ in range(b)]

    ans = solve(r, g, b, rs, gs, bs)
    print(ans)

if __name__ == "__main__":
    # 示例：运行规模 n = 5
    main(5)