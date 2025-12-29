def main(n: int):
    import random

    # 生成测试数据
    # a: 长度为 n 的随机数组，元素在 0..10^9 之间
    a = [random.randint(0, 10**9) for _ in range(n)]

    # 构造 Array，与原程序保持一致
    Array = [a]
    for _ in range(n - 1):
        prev = Array[-1]
        aux = []
        for j in range(1, len(prev)):
            aux.append(prev[j - 1] ^ prev[j])
        Array.append(aux)

    # 预处理最大值
    for j in range(1, len(Array)):
        row = Array[j]
        prev = Array[j - 1]
        for k in range(len(row)):
            row[k] = max(row[k], prev[k], prev[k + 1])

    # 根据 n 生成查询数量 q 以及查询区间
    # 示例策略：生成 n 个查询，每个查询随机选取 1 <= l <= r <= n
    q = n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 输出查询结果
    for l, r in queries:
        print(Array[r - l][l - 1])


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可根据需要修改规模
    main(5)