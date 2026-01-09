def main(n):
    # 生成确定性的测试数据：
    # 将输入规模 n 映射为 (n, k) 形式，其中 k 也与 n 确定性相关
    # 这里设定：
    #   原程序期望输入: 两个整数 n, k
    #   新程序: 使用传入的 n 作为第一个参数，
    #           使用 k = n // 2 作为第二个参数
    orig_n = n
    k = n // 2

    # 原始核心逻辑
    # numEat = n - ((sqrt(8*(n+k)+9) - 3) / 2)
    res = int(orig_n - ((8 * (orig_n + k) + 9) ** (1 / 2) - 3) / 2)
    # print(res)
    pass
    return res


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n 的大小做复杂度实验
    main(10)