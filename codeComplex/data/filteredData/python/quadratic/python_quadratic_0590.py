def check(ss, p):
    i = 0
    m = 10 ** 5
    ans = 0
    while i < len(p):
        if p[i] != ss[i]:
            ans += 1
        i += 1
    m = min(m, ans)
    ans = 0
    i = 1
    while i < len(p) + 1:
        if p[i - 1] != ss[i]:
            ans += 1
        i += 1
    m = min(m, ans)
    ans = 0
    i = 2
    while i < len(p) + 2:
        if p[i - 2] != ss[i]:
            ans += 1
        i += 1
    m = min(m, ans)
    return m


def main(n):
    sss = 'RGB' * 700
    # 规模映射：
    # n >= 3
    # n: 字符串长度
    # k: 子串长度 = max(1, n // 2)
    if n < 3:
        n = 3
    k = max(1, n // 2)

    # 构造确定性字符串 s，长度为 n，周期模式 'R','G','B','R','R',...
    base = "RGBR"
    s = "".join(base[i % len(base)] for i in range(n))

    m = 10 ** 5
    for i in range(n - k + 1):
        m = min(m, check(sss, s[i:i + k]))
    # print(m)
    pass
if __name__ == "__main__":
    main(1000)