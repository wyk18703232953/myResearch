def main(n: int):
    # 原逻辑开始（根据 n 计算第 n 位数字）
    x = 1

    # 第一部分：确定所在“位数段”（1~9, 10~99, 100~999 ...）
    while n > (10 ** (len(str(x)) - 1) * 9 * len(str(x))):
        n -= 10 ** (len(str(x)) - 1) * 9 * len(str(x))
        x *= 10

    t = len(str(x))
    nadighe = False

    # 第二部分：更细致地确定起始数字
    while nadighe is False:
        qw = 1
        nadighe = True
        while n > (10 ** (len(str(qw)) - 1) * 9 * t):
            n -= 10 ** (len(str(qw)) - 1) * 9 * t
            nadighe = False
            qw *= 10
        x += qw - 1

    # 第三部分：移动到具体的数字并找到对应的那一位
    while n > len(str(x)):
        n -= len(str(x))
        x += 1

    for i in range(len(str(x))):
        if n != 0:
            s = str(x)[i]
            n -= 1

    print(s)


if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据（这里直接使用 n 自身为规模）
    # 可在此处修改或批量测试不同的 n
    test_n = 250  # 示例规模，可自行调整
    main(test_n)