def main(n):
    # 映射：原程序中的 n 为对数数量，这里保持一致
    # 额外需要一个 k，令 1 <= k <= n，取确定性的 k = n//2 + 1（当 n>=1）
    if n <= 0:
        return 0

    k = n // 2 + 1
    if k > n:
        k = n

    # 生成确定性数据：n 行 (a, b)
    # 设计：a 从 1 到 n，b 为 (i % 5)，并在特定位置制造重复元素，便于 count 生效
    lst = []
    for i in range(1, n + 1):
        a = i
        b = i % 5
        # 构造一点重复模式：每隔 n//3 位置复制某个固定元素
        if n >= 3 and i % (n // 3 or 1) == 0:
            a = n // 2 or 1
            b = (n // 2) % 5
        lst.append([-a, b])

    lst.sort()
    # 若 k-1 越界则返回 0（理论上不会，因为 1<=k<=n）
    target = lst[k - 1]
    result = lst.count(target)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)