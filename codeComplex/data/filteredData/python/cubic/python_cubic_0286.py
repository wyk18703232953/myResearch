import random

# 全局变量声明（保持原代码结构）
r = g = b = 0
r_c = []
g_c = []
b_c = []
list_memo = []


def dp(ri, gi, bi):
    if ri > r or gi > g or bi > b:
        return 0

    if list_memo[ri][gi][bi] != -1:
        return list_memo[ri][gi][bi]

    res = 0
    # 配对 R-G
    if ri < r and gi < g:
        res = max(res, dp(ri + 1, gi + 1, bi) + r_c[ri] * g_c[gi])
    # 配对 R-B
    if ri < r and bi < b:
        res = max(res, dp(ri + 1, gi, bi + 1) + r_c[ri] * b_c[bi])
    # 配对 G-B
    if gi < g and bi < b:
        res = max(res, dp(ri, gi + 1, bi + 1) + g_c[gi] * b_c[bi])

    list_memo[ri][gi][bi] = res
    return res


def main(n):
    """
    n 为规模参数，用于生成 r, g, b 以及对应的数组长度。
    这里简单设定：
      r = n
      g = max(1, n-1)
      b = max(1, n-2)
    并随机生成颜色强度数据（正整数）。
    """
    global r, g, b, r_c, g_c, b_c, list_memo

    # 根据 n 设置各数组长度（可根据需求调整策略）
    r = n
    g = max(1, n - 1)
    b = max(1, n - 2)

    # 生成测试数据：1 到 100 之间的随机整数
    r_vals = [random.randint(1, 100) for _ in range(r)]
    g_vals = [random.randint(1, 100) for _ in range(g)]
    b_vals = [random.randint(1, 100) for _ in range(b)]

    # 按原逻辑排序并在末尾加 0（作为“空”颜色）
    r_c = sorted(r_vals + [0], reverse=True)
    g_c = sorted(g_vals + [0], reverse=True)
    b_c = sorted(b_vals + [0], reverse=True)

    # 重新计算 r, g, b（数组有效长度，包含末尾 0）
    r = len(r_c) - 1
    g = len(g_c) - 1
    b = len(b_c) - 1

    # 初始化记忆化数组
    list_memo = [[[-1] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    # 返回 dp 结果
    return dp(0, 0, 0)


if __name__ == "__main__":
    # 示例：规模为 5
    ans = main(5)
    print(ans)