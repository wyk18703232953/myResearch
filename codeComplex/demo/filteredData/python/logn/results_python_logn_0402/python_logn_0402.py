def main(n):
    # 根据原程序的输入结构：n, m, k, l 为四个整数
    # 将 n 作为第一个参数，其余三个参数由 n 确定性生成
    # 规模含义：n 为原始的 n，m、k、l 随 n 线性变化
    if n <= 0:
        # print(-1)
        pass
        return

    # 确定性生成 m, k, l
    m = max(1, n // 3 + 1)
    k = n // 2
    l = n // 4 + 1

    lb, rb = 0, n // m + 1
    while rb - lb > 1:
        mid = (lb + rb) >> 1

        if mid * m - k >= l:
            rb = mid

        else:
            lb = mid

    if lb != n // m:
        # print(rb)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小做时间复杂度实验
    main(10_000)