def main(n):
    # 将 n 解释为原问题中的 n，且设定 k 为 n//2 + 1，保证 1 <= k <= n
    if n <= 0:
        return
    k = max(1, min(n, n // 2 + 1))

    # 确定性生成长度为 n 的数组 a
    # 构造为一个严格递增序列，便于保持原逻辑语义（差分为非负）
    a = [i * 3 + (i // 2) for i in range(n)]

    t = []
    for i in range(1, n):
        t.append(a[i] - a[i - 1])
    t.sort()
    # 保证切片安全：当 n == 1 时，range(1, n) 为空，t 为空，n-k 至少为 0
    result = sum(t[:max(0, n - k)])
    print(result)


if __name__ == "__main__":
    # 示例：可修改 n 以进行规模化时间复杂度实验
    main(10)