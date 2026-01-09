def main(n):
    # 解释输入结构：
    # 原程序读取：n, m, a, b 四个整数
    # 我们将输入规模参数 n 用于构造这四个值，保证规模可控且行为确定
    #
    # 构造规则（完全确定性）：
    #   N = n
    #   M = 2 * n + 3
    #   A = n % 7 + 1
    #   B = (n % 5) + (n // 3) + 1
    #
    # 这样 N, M, A, B 都是 n 的确定性函数，可以用于不同 n 做时间复杂度实验

    N = n
    M = 2 * n + 3
    A = n % 7 + 1
    B = (n % 5) + (n // 3) + 1

    if N > M:
        if N % M == 0:
            # print(0)
            pass

        else:
            t1 = N % M
            # print(min(t1 * B, (M - t1) * A))
            pass
    elif N == M:
        # print(0)
        pass

    else:
        # print(min(N * B, (M - N) * A))
        pass
if __name__ == "__main__":
    # 示例：对若干不同规模调用 main(n)
    for test_n in [1, 5, 10, 100]:
        main(test_n)