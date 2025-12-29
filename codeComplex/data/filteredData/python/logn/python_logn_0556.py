def main(n: int):
    """
    使用规模 n 生成测试数据 k，并执行原逻辑：
    在无限数字串 123456789101112... 中找到第 k 位的数字。
    """
    # 生成测试数据：让 k 在 [1, n] 范围内取一个确定值
    # 这里简单设定 k = n（也可根据需要改为其他生成方式）
    k = max(1, n)

    for i in range(20):
        segment_len = 10 ** i * 9 * (i + 1)
        if k > segment_len:
            k -= segment_len
        else:
            a = (k - 1) // (i + 1) + 10 ** i
            b = (k - 1) % (i + 1)
            print(str(a)[b])
            break


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(1000)