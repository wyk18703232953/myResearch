def main(n):
    import random

    # 生成测试数据：b 为长度为 n 的整数数组，这里用 0/1 随机数作为示例
    # 可根据需要修改生成规则
    random.seed(0)  # 固定种子便于复现
    b = [random.randint(0, 1) for _ in range(n)]

    d = [[b[i] if i == j else -1 for i in range(n)] for j in range(n)]

    def f(i, j):
        if d[i][j] != -1:
            return d[i][j]
        d[i][j] = 0
        for m in range(i, j):
            l = f(i, m)
            if f(m + 1, j) == l and l:
                d[i][j] = l + 1
                break
        return d[i][j]

    a = [x for x in range(1, n + 1)]
    for e in range(1, n):
        for s in range(e + 1):
            if f(s, e):
                a[e] = min(a[e], (a[s - 1] + 1) if s > 0 else a[s])

    print(a[-1])


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)