def main(n):
    # 生成测试数据：构造长度为 n 的字符串 s 和一个 k 值
    # 这里示例：s 为前半部分 'ab' 重复，后面补 'c'；k 为 3
    # 你可以根据需要调整生成规则
    if n <= 0:
        return ""

    # 简单构造一个有前后缀结构的字符串，方便测试
    base = "ab"
    s = (base * (n // len(base))) + "c" * (n % len(base))
    s = s[:n]  # 确保长度刚好为 n

    k = 3  # 可以根据需要修改测试规模

    # 原逻辑开始（去掉 input，直接使用 s, n, k）
    s1 = s
    c = 0
    for i in range(len(s) - 1):
        if s[:i + 1] == s[n - i - 1:]:
            c = i + 1
    for _ in range(k - 1):
        s1 += s[c:]
    # print(s1)
    pass
    return s1


if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)