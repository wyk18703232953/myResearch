from sys import stdin


def main(n):
    # 1) 生成规模为 n 的测试数据 aa（这里用 1..n 的升序整数）
    aa = list(range(1, n + 1))

    # 2) 原逻辑：构建 dp
    dp = [aa]
    for i in range(n - 1, 0, -1):
        aa = aa[:]  # 复制当前层
        for j in range(i):
            aa[j] ^= aa[j + 1]
        del aa[-1]
        dp.append(aa)

    aa = dp[0]
    for i, bb in enumerate(dp[1:], 1):
        a = aa[0]
        for j, b in enumerate(bb):
            c = aa[j + 1]
            bb[j] = max(a, b, c)
            a = c
        aa = bb

    # 3) 生成查询数据。
    #    示例策略：对所有 1 <= lo <= hi <= n 生成一组完整查询
    queries = []
    for lo in range(1, n + 1):
        for hi in range(lo, n + 1):
            queries.append((lo, hi))

    # 4) 处理查询，输出结果
    res = []
    for lo, hi in queries:
        res.append(str(dp[hi - lo][lo - 1]))

    # print("\n".join(res))
    pass
if __name__ == '__main__':
    # 示例：运行 main(5) 以演示
    main(5)