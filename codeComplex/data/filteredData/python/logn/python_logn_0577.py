def main(n):
    i = 0
    s = 0
    while True:
        temp = (i + 1) * 9 * (10 ** i)
        if s + temp <= n:
            s += temp
            i += 1

        else:
            break

    tc = n - s
    nd = tc // (i + 1) - 1
    tc -= (nd + 1) * (i + 1)
    f = 10 ** i + nd  # 保留原逻辑中的中间量，便于理解和调试

    if tc != 0:
        # print(str(10 ** i + nd + 1)[tc - 1])
        pass

    else:
        # print(str(10 ** i + nd)[-1])
        pass


# 示例：根据 n 生成测试数据并调用
if __name__ == "__main__":
    # 这里可以根据需要指定 n 的规模，例如：
    # 小规模测试
    # n = 15
    # 中等规模
    # n = 1000
    # 大规模
    # n = 10**6

    # 示例固定一个 n 作为测试数据
    n = 1000
    main(n)