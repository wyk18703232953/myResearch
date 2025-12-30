def main(n):
    # 根据规模 n 生成测试数据，这里简单设定：
    # 让区间长度与 n 相关，例如区间长度为 n
    l = 0
    r = n

    if l == r:
        print(0)
    else:
        x = l ^ r
        c = 0
        while x > 0:
            x = x // 2
            c = c + 1
        print(2 ** c - 1)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(10)