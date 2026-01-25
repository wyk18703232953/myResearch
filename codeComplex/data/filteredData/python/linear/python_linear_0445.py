def main(n):
    # 映射 n 为字符串长度规模
    # 保证长度至少为 1
    n = max(1, int(n))

    # 构造 n 和 m，使得 m 与 b 的长度一致
    # 原代码中读入 n, m 但实际上只使用字符串本身做比较
    # 这里让 m = n，b 的长度也为 n
    m = n

    # 构造模式串 a，长度不超过 n
    # 使用可含 '*' 的确定性模式：
    # 当 n 为偶数：构造带 '*' 的模式
    # 当 n 为奇数：构造不带 '*' 的模式
    if n % 2 == 0:
        # 带通配符的模式：前半部分 + '*' + 后半部分
        prefix_len = n // 3
        suffix_len = n // 4
        prefix = ''.join(chr(ord('a') + (i % 3)) for i in range(prefix_len))
        suffix = ''.join(chr(ord('x') - (i % 3)) for i in range(suffix_len))
        a = prefix + '*' + suffix
    else:
        # 不带通配符的模式：全由字母构成
        a = ''.join(chr(ord('a') + (i % 3)) for i in range(min(n, 10)))

    # 构造文本串 b，长度为 m
    # 让其与 a 有时匹配，有时不匹配，保持确定性
    if '*' in a:
        a1, a2 = a.split('*')
        Len1 = len(a1)
        Len2 = len(a2)
        # 前缀部分
        b_prefix = a1
        # 中间填充部分
        middle_len = max(0, m - Len1 - Len2)
        middle = ''.join(chr(ord('k') + (i % 5)) for i in range(middle_len))
        # 后缀部分：根据 n 的奇偶变化一个字符以制造不一定匹配的情况
        if n % 4 == 0:
            b_suffix = a2
        else:
            if Len2 > 0:
                b_suffix = a2[:-1] + chr(ord(a2[-1]) + 1)
            else:
                b_suffix = ''
        b = b_prefix + middle + b_suffix
        b = b[:m]
    else:
        # 无 '*'，b 有时等于 a，有时不等
        base = ''.join(chr(ord('a') + (i % 3)) for i in range(m))
        if n % 3 == 0:
            # 使得 b == a（在长度允许的范围内）
            if len(a) >= m:
                b = a[:m]
            else:
                b = a + base[len(a):]
        else:
            # 使得 b 与 a 至少一处不同
            if m == 0:
                b = ''
            else:
                b_list = list(base)
                b_list[0] = chr(ord(b_list[0]) + 1)
                b = ''.join(b_list)

    # 原算法逻辑
    flag = 0
    for c in a:
        if c == '*':
            flag = 1
    if flag == 1:
        a1, a2 = a.split('*')
        Len1 = len(a1)
        Len2 = len(a2)
        b1 = b[:Len1]
        b2 = ''
        if Len2:
            b2 = b[-Len2:]
        if a1 == b1 and a2 == b2 and Len1 + Len2 <= len(b):
            print('YES')
        else:
            print('NO')
    else:
        if a == b:
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的规模
    main(10)