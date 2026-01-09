def main(n):
    # 为了进行时间复杂度实验，这里将 n 解释为原程序中第一个参数 n。
    # 其余参数 m, k, l 根据 n 确定性生成。
    # 例如：
    #   m = max(1, n // 3)
    #   k = n // 2
    #   l = n // 4
    m = max(1, n // 3)
    k = n // 2
    l = n // 4

    if (k + l + m - 1) // m * m > n:
        # print(-1)
        pass

    else:
        # print((k + l + m - 1) // m)
        pass
if __name__ == "__main__":
    # 示例：使用 n = 100 作为输入规模
    main(100)