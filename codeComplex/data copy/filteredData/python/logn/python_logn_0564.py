def main(n: int):
    # 根据规模 n 生成测试数据：这里直接用 n 作为原程序的输入
    # 原程序读取的值记为 m
    m = n

    # 原始逻辑开始
    n = m - 1
    x = 1
    y = 9
    while n > x * y:
        n -= x * y
        y *= 10
        x += 1
    a = 10 ** (x - 1)
    a += n // x
    ans = str(a)[n % x]

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：可在此处指定规模 n 进行测试
    main(100)