def main(n):
    # 输入结构：单行四个整数 n, m, k, l
    # 将参数 n 视为原程序中的 n 的规模，其余参数按照确定性规则生成
    # 这里生成：
    #   original_n = n
    #   m = max(1, n // 3)
    #   k = n // 2 + 1
    #   l = n // 4 + 1
    original_n = n
    m = max(1, n // 3)
    k = n // 2 + 1
    l = n // 4 + 1

    q = (l + k - 1) // m + 1
    if q * m > original_n:
        # print(-1)
        pass

    else:
        # print(q)
        pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 的大小进行时间复杂度实验
    main(10)