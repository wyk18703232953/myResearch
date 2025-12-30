def main(n):
    # 依据规模 n 生成测试数据 (n, k)
    # 该原题逻辑要求：若 1 + k*(k-1)//2 < n 则无解(-1)
    # 为保证有解，这里构造 k 使得 1 + k*(k-1)//2 >= n
    # 取 k 为满足上述不等式的最小整数
    # 解 k^2 - k - 2(n-1) >= 0
    import math

    if n <= 0:
        print(-1)
        return

    if n == 1:
        print(0)
        return

    # 求 k
    k = int((1 + math.isqrt(1 + 8 * (n - 1)) + 1) // 2)  # 稍微向上取一点
    # 调整保证 1 + k*(k-1)//2 >= n
    while 1 + k * (k - 1) // 2 < n:
        k += 1

    # 原始逻辑开始
    if n == 1:
        print(0)
        return
    if 1 + k * (k - 1) // 2 < n:
        print(-1)
        return

    l, r = 0, k - 1
    while l < r:
        m = (l + r + 1) // 2
        if 1 + (m + k - 1) * (k - 1 - m + 1) // 2 >= n:
            l = m
        else:
            r = m - 1

    if 1 + (l + k - 1) * ((k - 1) - l + 1) // 2 < n:
        print(k - 1 - l + 2)
    else:
        print(k - 1 - l + 1)


# 示例调用
if __name__ == "__main__":
    # 可根据需要修改 n
    main(10)