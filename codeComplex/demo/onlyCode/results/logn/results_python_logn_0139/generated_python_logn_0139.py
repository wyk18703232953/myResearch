def main(n):
    # 根据规模 n 生成测试数据：
    # 这里随机构造一个与 n 同阶的 k，使得 1 + k*(k-1)//2 >= n
    # 为了简单与可重复，这里直接取 k 为满足 1 + k*(k-1)//2 >= n 的最小整数
    k = 1
    while 1 + k * (k - 1) // 2 < n:
        k += 1

    # 原逻辑开始
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


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要修改
    main(10)