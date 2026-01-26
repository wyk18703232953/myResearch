def main(n):
    # 解释原输入结构：
    # 原程序从一行读入：n, m, k, l
    # 为了规模化与确定性实验，这里：
    #   - 保留原变量名：N, m, k, l
    #   - 将参数 n 作为原变量 N 的规模基础
    #   - 构造 m, k, l 为 n 的简单确定性函数
    #
    # 生成规则（完全确定性）：
    #   N = n
    #   m = max(1, n // 3)
    #   k = n // 4
    #   l = n // 5
    #
    # 注意：不使用任何随机数或外部输入

    N = n
    m = max(1, n // 3)
    k = n // 4
    l = n // 5

    if l > N - k:
        # print(-1)
        pass

    else:
        am = ((l + k) // m + bool((l + k) % m))
        if am * m > N:
            # print(-1)
            pass

        else:
            # print(am)
            pass
if __name__ == "__main__":
    # 示例调用：可自行修改 n 以进行不同规模测试
    main(1000)