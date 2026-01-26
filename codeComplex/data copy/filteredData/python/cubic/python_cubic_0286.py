def main(n):
    # n 控制每种颜色的数量规模
    r = max(1, n)
    g = max(1, n)
    b = max(1, n)

    # 确定性生成数据：简单的递减序列，保证排序后仍确定
    r_c = [i for i in range(r, 0, -1)]
    g_c = [i * 2 for i in range(g, 0, -1)]
    b_c = [i * 3 for i in range(b, 0, -1)]

    # 原程序在读入后会在每个数组后加一个 0 并按降序排序
    r_c = sorted(r_c + [0], reverse=True)
    g_c = sorted(g_c + [0], reverse=True)
    b_c = sorted(b_c + [0], reverse=True)

    # 将必要的变量放入闭包环境，保持原逻辑
    R, G, B = r, g, b
    list_memo = [[[-1] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]

    def dp(ri, gi, bi):
        if ri > R or gi > G or bi > B:
            return 0
        if list_memo[ri][gi][bi] != -1:
            return list_memo[ri][gi][bi]
        res = max(
            dp(ri + 1, gi + 1, bi) + r_c[ri] * g_c[gi],
            dp(ri + 1, gi, bi + 1) + r_c[ri] * b_c[bi],
            dp(ri, gi + 1, bi + 1) + g_c[gi] * b_c[bi],
        )
        list_memo[ri][gi][bi] = res
        return res

    return dp(0, 0, 0)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    result = main(5)
    # print(result)
    pass