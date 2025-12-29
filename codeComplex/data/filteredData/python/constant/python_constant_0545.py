def main(n):
    # 根据 n 生成测试数据：
    # 原程序读取：n, s = num()
    # 这里我们令 s 为与 n 同数量级的值，例如 s = n*(n+1)//2
    s = n * (n + 1) // 2

    cc = 0
    for i in range(n, 0, -1):
        cc += s // i
        s = s % i
    print(cc)


if __name__ == "__main__":
    # 示例：可以修改这里的 n 以测试不同规模
    main(10)