def main(n):
    # 生成确定性字符串，长度为 n
    # 使用循环模式 "abca"，避免全部相同导致退化
    pattern = "abca"
    s = "".join(pattern[i % len(pattern)] for i in range(n))

    c = 0
    c1 = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - i - 1]:
            c += 1
    for i in range(len(s)):
        if s[i] == s[0]:
            c1 += 1
    if c1 == len(s):
        # print(0)
        pass
    elif c == len(s) // 2:
        # print(len(s) - 1)
        pass

    else:
        # print(len(s))
        pass
if __name__ == "__main__":
    main(10)