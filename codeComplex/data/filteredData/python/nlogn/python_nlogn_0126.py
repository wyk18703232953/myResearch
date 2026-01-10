def main(n):
    # 映射含义：
    # n -> 原程序中的 n（数组长度）
    # m, k 由 n 确定性生成
    # a 为长度为 n 的整数数组

    # 生成 m 和 k，保证 1 <= k <= m 且随 n 可扩展
    m = max(1, 3 * n)
    k = max(1, n // 2)

    # 生成数组 a，长度为 n，元素为确定性的正整数
    # 示例：a[i] = (i % 7) + 1，保证都有正贡献
    a = [(i % 7) + 1 for i in range(n)]

    # 原始逻辑
    a.sort(reverse=True)
    i = 0
    while k < m and i < n:
        k += a[i] - 1
        i += 1
    result = i if k >= m else -1

    print(result)


if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次可重复的规模化实验
    main(10)