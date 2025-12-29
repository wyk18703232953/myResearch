def main(n):
    # 这里将原本的 n, k 输入改为基于规模 n 的测试数据生成逻辑
    # 可根据需要调整生成策略，这里简单设定 k = n
    k = n

    # 以下为原程序逻辑（去掉 input()，用参数与生成数据替代）
    n, k = n - 1, k - 1
    l = 0
    r = k
    g = k * (k + 1) // 2
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if (g - m * (m + 1) // 2) >= n:
            ans = k - m
            l = m + 1
        else:
            r = m - 1
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)