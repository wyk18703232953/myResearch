def main(n):
    # 映射规则：
    # 原程序需要 n, m, k, l 四个整数
    # 这里将调用参数 n 作为原始的 n
    # 其余 m, k, l 由 n 确定性构造
    orig_n = n
    m = max(1, n // 3)        # 保证 m >= 1
    k = n // 2
    l = n // 4

    k += l
    x = (k + m - 1) // m
    if m * x > orig_n:
        # print(-1)
        pass

    else:
        # print(x)
        pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 的大小进行时间复杂度实验
    main(10)