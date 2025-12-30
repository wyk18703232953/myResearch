def main(n):
    # 生成规模为 n 的测试数据
    # 原程序读入：n, q；接着 n 个数组元素；接着 q 个查询
    # 这里我们构造：
    #   - 数组 a 为 1..n 的升序
    #   - 查询 Q 为 1..n 的所有查询（q = n）
    q = n
    a = list(range(1, n + 1))
    Q = list(range(1, q + 1))

    # 原逻辑开始
    if q == 0:
        return

    sq = set(Q)
    mx = max(Q)
    d = dict()
    ch = 1

    for i in range(min(mx, n + 1)):
        if ch == n:
            ch = 1
        if i + 1 in sq:
            d[i + 1] = [a[0], a[ch]]
        if a[0] < a[ch]:
            a[0], a[ch] = a[ch], a[0]
        ch += 1

    # 收集输出结果并返回（避免直接 print，便于测试）
    results = []
    for i in Q:
        if i > n:
            x = n - 1 if i % (n - 1) == 0 else i % (n - 1)
            results.append((a[0], a[x]))
        else:
            results.append(tuple(d[i]))
    return results


if __name__ == "__main__":
    # 示例运行：n = 5，可按需修改
    out = main(5)
    for pair in out:
        print(*pair)