def main(n: int):
    # 生成测试数据：
    # a: 一个长度为 n 的数组，元素为 1..n 的逆序，用于产生大量逆序对
    # m: 查询次数，设为 n（可根据需要调整）
    # 每个查询区间 [l, r] 使得 (r-l+1) 大致有一半是奇数长度，保持多样性
    a = list(range(n, 0, -1))  # 逆序数组
    m = n

    # 原逻辑开始
    c = 0
    for i in range(1, n):
        for j in range(i):
            if a[j] > a[i]:
                c += 1
    c = c % 2

    outputs = []
    for i in range(m):
        # 构造查询区间：
        # 让区间长度在 1..n 范围内循环分布
        length = (i % n) + 1
        l = 0
        r = min(n - 1, l + length - 1)

        s = (r - l + 1) // 2
        if s % 2 == 1:
            c = (c + 1) % 2
        if c == 0:
            outputs.append("even")

        else:
            outputs.append("odd")

    # 按行输出结果
    for line in outputs:
        # print(line)
        pass
if __name__ == "__main__":
    # 示例：调用 main(5) 进行简单测试
    main(5)