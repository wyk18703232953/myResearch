def main(n: int):
    # 生成测试数据：根据规模 n 构造 a, b
    # 这里示例为：
    #   a = n
    #   b = n*(n+1)//4   （任选一类合理生成方式即可）
    a = n
    b = n * (n + 1) // 4

    l = 0
    r = a + 1
    while r - l > 1:
        m = (r + l) // 2
        if m * (m + 1) // 2 - (a - m) > b:
            r = m

        else:
            l = m
    # print(a - l)
    pass
if __name__ == "__main__":
    # 示例调用
    main(10)