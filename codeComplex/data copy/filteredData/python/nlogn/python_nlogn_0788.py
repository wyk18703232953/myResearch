def main(n):
    # 映射：原始输入中的 n 为数组长度，这里用参数 n 表示数组长度
    # 固定生成 k，保证 1 <= k <= n
    if n <= 0:
        # print(0)
        pass
        return

    k = n // 2 + 1  # 合理选择 k，使得随着 n 变化有意义
    if k > n:
        k = n

    # 确定性生成数组 a，长度为 n
    # 示例：a[i] = i * 2 + (i // 3)
    a = [i * 2 + (i // 3) for i in range(n)]

    b = []
    for i in range(n - 1):
        b.append(a[i + 1] - a[i])
    b.sort()
    result = sum(b[:len(b) - k + 1])
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行规模实验
    main(10)