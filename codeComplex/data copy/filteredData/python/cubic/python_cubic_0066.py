def cnt(s, t):
    i, c = 0, 0
    while s.count(t):
        s = s[s[i:].index(t) + 1:]
        c += 1
    return c

def main(n):
    # 生成规模为 n 的测试数据：重复模式方便出现多次子串
    # 例如循环使用小写字母
    import string
    base = string.ascii_lowercase
    s = ''.join(base[i % len(base)] for i in range(n))

    length = len(s)
    ln = 0
    for i in range(length):
        for j in range(i, length):
            if (j - i + 1) <= ln:
                continue
            if cnt(s, s[i:j + 1]) >= 2:
                ln = max(ln, j - i + 1)
    # print(ln)
    pass
if __name__ == "__main__":
    # 示例：调用 main(20)，可按需修改 n
    main(20)