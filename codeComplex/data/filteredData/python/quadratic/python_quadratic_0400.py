def main(n):
    # 将 n 映射为字符串长度和重复次数，保证确定性与可扩展性
    length = max(1, n)
    k = max(1, n // 3)

    # 构造确定性的字符串 s，由小写字母循环组成
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s_chars = [alphabet[i % 26] for i in range(length)]
    s = "".join(s_chars)

    s1 = s
    c = 0
    for i in range(len(s) - 1):
        if s[:i + 1] == s[length - i - 1:]:
            c = i + 1
    for _ in range(k - 1):
        s1 += s[c:]
    print(s1)


if __name__ == "__main__":
    main(10)