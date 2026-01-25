def main(n):
    # 对应原程序中的 n（字符串长度）和 k（重复次数）
    # 这里将 n 作为字符串长度，k 定义为 n 的一个确定性函数
    if n <= 0:
        return

    k = n // 2 + 1  # 保证 k >= 1，且随 n 增长

    # 构造确定性的字符串 s，长度为 n
    # 使用重复的固定字符序列
    base = "abc"
    s = "".join(base[i % len(base)] for i in range(n))

    ap = 0
    i = 1
    while i < n:
        if s[:i] == s[-i:]:
            ap = i
        i += 1

    result = s + s[ap:] * (k - 1)
    print(result)


if __name__ == "__main__":
    # 示例调用，使用一个确定的 n
    main(10)