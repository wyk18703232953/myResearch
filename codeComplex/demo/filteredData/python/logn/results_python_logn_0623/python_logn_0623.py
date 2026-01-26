def main(n: int):
    # 生成测试数据：根据规模 n 构造一个 k
    # 这里我们令 k 为 n*(n+1)//4（大约是最大可实现值的一半）
    k = n * (n + 1) // 4

    low, high = 0, n

    # 二分搜索满足 (n - eaten) * (n - eaten + 1) / 2 - eaten < k 的最大 eaten
    while low <= high:
        eaten = (low + high) // 2
        added = (n - eaten) * (n - eaten + 1) / 2

        if added - eaten >= k:
            low = eaten + 1

        else:
            high = eaten - 1

    # print(high)
    pass
if __name__ == "__main__":
    # 可在此修改 n 进行本地测试
    main(10)