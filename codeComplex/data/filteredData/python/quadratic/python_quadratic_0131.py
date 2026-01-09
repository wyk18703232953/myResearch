def main(n):
    # 映射：原程序中
    # n -> 元素个数
    # m -> 取值范围（这里设为 n）
    # 后续一行有 n 个整数，每个在 [1, m] 范围内
    m = n

    # 生成输入数据：n 个整数，完全确定性
    # 使用 i % m + 1 形成较均匀分布
    data = [(i % m) + 1 for i in range(n)]

    # 原程序逻辑开始
    q = {}
    for i in range(1, n + 1):
        q[i] = 0
    for x in data:
        if x in q:
            q[x] += 1
    res = min(q.values()) if q else 0
    # print(res)
    pass
if __name__ == "__main__":
    main(10)