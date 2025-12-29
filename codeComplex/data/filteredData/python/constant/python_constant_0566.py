def main(n):
    """
    按题意：原程序为
        n, m, k, l = map(int, input().split())
        if m > n or (l + k + m - 1) // m * m > n:
            print(-1)
        else:
            x = (l + k + m - 1) // m
            print(x)

    这里根据给定规模 n 自动生成 m, k, l 测试数据。
    可按需要调整生成策略。
    """
    # 生成一组与 n 相关的测试数据：
    # 让 1 <= m <= n，k 和 l 与 n 同量级
    if n <= 0:
        return  # 不做任何输出

    m = max(1, n // 3)       # 保证 1 <= m <= n
    k = n // 2               # 随机构造：与 n 同量级
    l = n // 4               # 随机构造：与 n 同量级

    # 原逻辑
    if m > n or ((l + k + m - 1) // m) * m > n:
        print(-1)
    else:
        x = (l + k + m - 1) // m
        print(x)


# 示例调用
if __name__ == "__main__":
    # 这里给一个示例规模，可在实际使用时由外部调用 main(n)
    main(100)