def main(n):
    # 生成确定性输入：
    # 原程序输入：
    #   n: 一个整数
    #   s2: 一个字符串（长度至少为 n），由 '0'~'9' 组成
    #
    # 我们将 n 直接作为原程序的 n；
    # s2 构造为长度 n 的数字字符串，模式为 (i % 10)，形成可控规模。
    if n <= 0:
        n = 1

    # 构造 s2：'1234567890123...' 的前 n 个字符
    s2 = ''.join(str(i % 10) for i in range(1, n + 1))

    # ===== 以下为在不依赖输入情况下复现原始核心逻辑 =====
    s2_list = list(s2)
    s = []
    for i in range(n):
        if s2_list[i] == '0':
            continue

        else:
            s.append(int(s2_list[i]))
    s1 = sum(s)
    n2 = len(s)
    l = []
    for i in range(2, n2 + 1):
        if s1 % i == 0:
            l.append(s1 // i)
    f = 0
    if len(s) == 0:
        f = 1
    for i in range(len(l)):
        c = 0
        if f == 1:
            break
        for j in range(n2):
            c += s[j]
            if c == l[i]:
                c = 0
                if j == n2 - 1:
                    f = 1
            elif c < l[i]:
                c = c

            else:
                break
    if f == 0:
        # print('NO')
        pass

    else:
        # print('YES')
        pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 的大小以做时间复杂度实验
    main(10)