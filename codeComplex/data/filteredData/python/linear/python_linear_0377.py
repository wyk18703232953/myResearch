def main(n):
    # 生成确定性的输入字符串 a，长度为 n
    # 模式：根据下标 i 对 3 取模生成 '0','1','2'
    chars = []
    for i in range(n):
        r = i % 3
        if r == 0:
            chars.append('0')
        elif r == 1:
            chars.append('1')
        else:
            chars.append('2')
    a = ''.join(chars)

    c1 = a.count('1')
    parts = a.split('2')
    lex = '0' * parts[0].count('0') + '1' * c1
    m = len(parts)
    for i in range(1, m):
        lex = lex + '2' + '0' * parts[i].count('0')
    print(lex)


if __name__ == "__main__":
    main(50)