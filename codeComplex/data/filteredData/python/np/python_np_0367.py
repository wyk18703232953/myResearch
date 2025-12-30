from random import randint


def main(n):
    # 生成测试数据：
    # 根据原程序结构，需生成:
    #   T: 测试组数
    #   对每组：n 行，m 列，以及 A 矩阵
    #
    # 这里约定：
    #   - T 固定为 1
    #   - 行数 = n
    #   - 列数 m 与 n 同规模，设为 n
    #   - A[i][j] 为 1~100 的随机整数
    T = 1
    m = n
    test_cases = []
    for _ in range(T):
        A = [[randint(1, 100) for _ in range(m)] for _ in range(n)]
        test_cases.append((n, m, A))

    # 原逻辑封装
    for (n, m, A) in test_cases:
        ans = 0
        for _ in range(100):
            for j in range(m):
                x = randint(0, n - 1)
                if x:
                    # 抽取列 j
                    B = [A[i][j] for i in range(n)]
                    # 旋转
                    B = B[x:] + B[:x]
                    # 写回列 j
                    for i in range(n):
                        A[i][j] = B[i]
            c = 0
            for i in range(n):
                c += max(A[i])
            ans = max(ans, c)
        print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)