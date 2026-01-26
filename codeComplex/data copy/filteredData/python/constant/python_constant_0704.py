def main(n):
    # 生成测试数据：
    # 这里假设 v 与 n 同规模，设置为 v = n // 2 作为示例
    v = n // 2

    # 原始逻辑开始
    primo = min(n - 1, v)
    if primo == n - 1:
        result = primo

    else:
        rimane = n - primo
        result = primo - 1 + (rimane) * (rimane + 1) // 2

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)