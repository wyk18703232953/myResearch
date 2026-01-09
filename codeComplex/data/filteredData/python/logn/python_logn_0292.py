def main(n):
    mod = 10**9 + 7

    # 确定性生成 x, k
    # 将 n 映射为 x, k，确保对任意 n 都有定义良好的输入规模
    # 这里选择：
    #   x = n
    #   k = 2*n + 3
    x = n
    k = 2 * n + 3

    if x == 0:
        # print(0)
        pass
        return

    result = (pow(2, k + 1, mod) * x % mod - (pow(2, k, mod) - 1)) % mod
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：可以根据需要修改 n 来进行时间复杂度实验
    main(10)