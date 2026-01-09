def main(n):
    # 这里的 n 作为“输入规模”，我们用它来构造一组确定性的 (n, s)
    # 为了让运算有意义，生成的 n_input 必须 > 0
    n_input = max(1, n)
    # s 随着规模线性增长，保持确定性
    s_input = 3 * n_input + 5

    # 原始逻辑开始
    if s_input % n_input == 0:
        result = s_input // n_input

    else:
        result = s_input // n_input + 1

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模
    main(10)