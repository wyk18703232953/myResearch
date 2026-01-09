def main(n):
    # 数据生成：原题结构为：
    # 第一行：n
    # 第二行：n 个整数
    # 这里用确定性的方式生成长度为 n 的整数序列
    # 例如：a[i] = i - n//2，确保有正有负有零
    a = [i - n // 2 for i in range(n)]

    # 原程序逻辑开始
    transformed = []
    for i in a:
        if abs(-i - 1) > abs(i):
            transformed.append(-i - 1)

        else:
            transformed.append(i)

    c = 0
    for x in transformed:
        if x < 0:
            c += 1

    if c % 2:
        me = 0
        for i in range(len(transformed)):
            if transformed[i] < transformed[me]:
                me = i
        transformed[me] = -transformed[me] - 1

    # 输出与原程序一致：空格分隔的一行
    # print(*transformed)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 以做时间复杂度实验
    main(10)