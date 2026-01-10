def main(n):
    # 生成确定性的字符串列表，长度为 n
    # 第 i 个字符串为由 'a' 到第 (i % 26) 个字母重复 (i+1) 次构成
    base_chars = [chr(ord('a') + i % 26) for i in range(n)]
    s = [base_chars[i] * (i + 1) for i in range(n)]

    for i in s:
        for j in s:
            if (i not in j) and (j not in i):
                print('NO')
                return

    print('YES')
    s = sorted(s, key=lambda x: len(x))
    for pal in s:
        print(pal)


if __name__ == "__main__":
    main(5)