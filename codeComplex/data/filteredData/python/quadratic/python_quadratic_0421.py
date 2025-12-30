def main(n):
    # 根据 n 生成测试数据：构造一个有前后缀重叠结构的字符串 s 和一个整数 k
    # 例如：s = "ab" * n + "a"（长度约 2n+1），k = n
    s = "ab" * n + "a"
    k = n

    p = len(s) - 1
    while p > 0 and s[:p] != s[-p:]:
        p -= 1
    print(s + s[p:] * (k - 1))


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)