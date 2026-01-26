def main(n):
    # 映射说明：
    # 原程序输入：n, m; 第二行是长度为 m 的整数列表
    # 在这里：n 为原程序的 n，m 也取为 n，使规模由 n 控制
    m = n

    # 构造长度为 m 的列表，对应原来的第二行输入
    # 使用简单确定性模式：循环 1..n
    # 这样 1..n 每个数字出现一次，保证统计行为合理
    daf1 = [i % n + 1 for i in range(m)]

    # 原始逻辑开始
    daf2 = dict()

    for i in range(n):
        daf2[i + 1] = 0

    for i in daf1:
        if i in daf2.keys():
            daf2[i] += 1

    # print(min(daf2.values()))
    pass
if __name__ == "__main__":
    main(10)