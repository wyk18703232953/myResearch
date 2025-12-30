def main(n):
    # 生成测试数据：给定规模 n，构造一个合理的 k
    # 这里构造 k 为总糖果数的一半（可根据需要调整生成策略）
    total_candies = n * (n + 1) // 2
    k = total_candies // 2

    l = 1
    r = n + 1

    # 二分查找原逻辑
    while r - l != 1:
        m = (l + r) >> 1
        candies = m * (m + 1) // 2
        eat = n - m

        if candies - eat <= k:
            l = m
        else:
            r = m

    ans = n - l
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)