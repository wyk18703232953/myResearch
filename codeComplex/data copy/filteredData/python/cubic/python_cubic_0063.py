def main(n):
    # 确定性生成字符串 s，长度为 n
    # 使用周期性模式构造
    base = "abcde"
    s = "".join(base[i % len(base)] for i in range(n))

    n_len, m = len(s), 0
    for i in range(n_len - 1):
        for j in range(i, n_len + 1):
            if len(s[i:j]) > m and s[i:j] in s[i + 1:n_len]:
                m = len(s[i:j])
    # print(m)
    pass
if __name__ == "__main__":
    main(10)