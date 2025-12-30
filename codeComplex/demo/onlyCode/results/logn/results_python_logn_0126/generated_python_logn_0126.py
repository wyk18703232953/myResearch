def main(n):
    # 根据规模 n 生成测试数据，这里简单设定 k = n
    # 可根据需要自行修改生成规则
    k = n

    if n == 1:
        print(0)
    elif k + (k - 1) * (k - 2) // 2 < n:
        print(-1)
    else:
        l = 0
        r = k - 1
        while r - l > 1:
            m = (l + r) // 2
            if (2 * k - m + 1) * m // 2 - (m - 1) >= n:
                r = m
            else:
                l = m
        print(r)


if __name__ == "__main__":
    # 示例：运行规模 n = 10
    main(10)