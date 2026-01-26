def main(n):
    # n 用作三个字符串的长度和算法中的原始 n
    l = max(1, n)

    # 构造三个确定性的只包含大小写字母的字符串
    # 使用循环序列确保覆盖 A-Z, a-z
    letters = []
    for i in range(26):
        letters.append(chr(65 + i))  # A-Z
    for i in range(26):
        letters.append(chr(97 + i))  # a-z
    base = ''.join(letters)  # 长度 52

    # 通过重复和截断生成长度为 l 的字符串
    def build_string(offset):
        s = []
        for i in range(l):
            s.append(base[(i + offset) % len(base)])
        return ''.join(s)

    st_a = build_string(0)
    st_b = build_string(1)
    st_c = build_string(2)

    a = [0 for _ in range(125)]
    b = [0 for _ in range(125)]
    c = [0 for _ in range(125)]

    for i in range(l):
        a[ord(st_a[i])] += 1
        b[ord(st_b[i])] += 1
        c[ord(st_c[i])] += 1

    maxi_a = 0
    maxi_b = 0
    maxi_c = 0

    if n == 1:
        maxi_a = max(a) + 1
        maxi_b = max(b) + 1
        maxi_c = max(c) + 1
        if maxi_a > l:
            maxi_a -= 2
        if maxi_b > l:
            maxi_b -= 2
        if maxi_c > l:
            maxi_c -= 2

    else:
        for i in range(123):
            if (65 <= i <= 90) or (97 <= i <= 122):
                if a[i] + n >= l:
                    maxi_a = max(maxi_a, l)

                else:
                    maxi_a = max(maxi_a, a[i] + n)
                if b[i] + n >= l:
                    maxi_b = max(maxi_b, l)

                else:
                    maxi_b = max(maxi_b, b[i] + n)
                if c[i] + n >= l:
                    maxi_c = max(maxi_c, l)

                else:
                    maxi_c = max(maxi_c, c[i] + n)

    s = [maxi_a, maxi_b, maxi_c]
    s.sort()
    if s[1] == s[2]:
        # print("Draw")
        pass
    if maxi_a > max(maxi_b, maxi_c):
        # print("Kuro")
        pass
    if maxi_b > max(maxi_c, maxi_a):
        # print("Shiro")
        pass
    if maxi_c > max(maxi_b, maxi_a):
        # print("Katie")
        pass
if __name__ == "__main__":
    main(10)