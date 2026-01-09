def main(n):
    # 生成确定性字符串 a，长度为 n，由字符 '0','1','2' 组成
    # 模式：根据位置 i 构造 0/1/2，确保包含多种情况
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
    # print(lex)
    pass
if __name__ == "__main__":
    main(1000)