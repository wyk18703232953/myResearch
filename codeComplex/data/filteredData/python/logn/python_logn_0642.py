def main(n: int):
    # 生成测试数据：给定规模 n，构造一个合理的 k
    # 原问题逻辑：寻找最大 m，使得 m(m+1)/2 - (n-m) <= k
    # 这里我们让 k 为大约一半规模的值，便于触发二分逻辑
    k = n // 2

    l = 1
    r = n + 1

    while r - l != 1:
        m = (l + r) >> 1
        candies = m * (m + 1) // 2
        eat = n - m

        if candies - eat <= k:
            l = m
        else:
            r = m

    # 保持与原程序相同的输出行为
    print(n - l)


if __name__ == "__main__":
    # 示例：运行 main，使用某个规模 n
    main(10)