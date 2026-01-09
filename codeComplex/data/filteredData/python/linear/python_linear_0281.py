def main(n):
    # n 表示输入规模，这里用来生成确定性的 n, m, a, b
    # 为保证 m 不为 0，令 m = n + 1
    N = n + 2          # 模拟原始输入中的 n
    M = n + 1          # 模拟原始输入中的 m
    A = n + 3          # 模拟原始输入中的 a
    B = n + 4          # 模拟原始输入中的 b

    x = N % M
    result = min(A * (M - x), B * x)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)