def main(n):
    # 生成确定性的字符串输入，长度为 n
    # 使用重复模式 'abc' 来构造字符串
    base = 'abc'
    s = ''.join(base[i % len(base)] for i in range(n))

    m = 0
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if len(s[i:j]) > m and s[i:j] in s[i + 1:len(s)]:
                m = len(s[i:j])
    # print(m)
    pass
if __name__ == "__main__":
    main(10)