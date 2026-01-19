def main(n):
    # 参数生成：l, r, x 与原始逻辑保持一致含义
    # 这里令：
    # x = max(1, n // 3)
    # l = n * (n + 1) // 4
    # r = n * (n + 1) // 2
    # 数组 a 为 1..n 的整数序列
    if n <= 0:
        print(0)
        return

    x = max(1, n // 3)
    l = n * (n + 1) // 4
    r = n * (n + 1) // 2
    a = [i + 1 for i in range(n)]

    count = 0
    # 遍历所有非空子集：位掩码从 1 到 2**n - 1
    for mask in range(1, 2 ** n):
        temp = []
        for j in range(n):
            if mask & (1 << j):
                temp.append(a[j])

        if temp:
            diff = max(temp) - min(temp)
            s = sum(temp)
            if diff >= x and l <= s <= r:
                count += 1

    print(count)


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 进行复杂度实验
    main(10)