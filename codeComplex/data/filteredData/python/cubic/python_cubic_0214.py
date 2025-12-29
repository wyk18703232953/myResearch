import random

def main(n: int):
    # 生成测试数据：rr, gg, bb 不超过 n
    rr = random.randint(0, n)
    gg = random.randint(0, n)
    bb = random.randint(0, n)

    # 每个颜色数组长度分别为 rr, gg, bb，元素为 1..n 的随机整数
    r = [random.randint(1, n) for _ in range(rr)]
    g = [random.randint(1, n) for _ in range(gg)]
    b = [random.randint(1, n) for _ in range(bb)]

    inf = 114514
    r = r + [inf]
    g = g + [inf]
    b = b + [inf]
    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    # dp[i][j][k] 定义与原程序一致
    dp = []
    for _ in range(rr + 1):
        dp.append([[0] * (bb + 1) for _ in range(gg + 1)])

    ans = 0
    for i in range(rr + 1):
        ri = r[i]
        for j in range(gg + 1):
            gj = g[j]
            for k in range(bb + 1):
                bk = b[k]
                if (i + j + k) % 2:
                    continue
                dpijk = 0
                if i > 0 and j > 0:
                    dpijk = max(dp[i - 1][j - 1][k] + ri * gj, dpijk)
                if j > 0 and k > 0:
                    dpijk = max(dp[i][j - 1][k - 1] + gj * bk, dpijk)
                if k > 0 and i > 0:
                    dpijk = max(dp[i - 1][j][k - 1] + bk * ri, dpijk)
                dp[i][j][k] = dpijk
                if ans < dpijk:
                    ans = dpijk

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 50
    main(50)