def main(n):
    # n 表示字符串数量规模
    if n <= 0:
        return

    # 确定性生成 n 个字符串，长度和内容由 n 和索引唯一决定
    # 结构：用字符序列和数字构造，避免非确定性
    uk = []
    for i in range(n):
        length = (i % 7) + 1  # 字符串长度在 1~7 之间循环
        base_char = chr(ord('a') + (i % 26))
        s = []
        for j in range(length):
            # 组合字母与数字，保证 determinism 且有一定多样性
            c = chr(ord('a') + ((i + j) % 26))
            d = str((i * 31 + j * 17 + n) % 10)
            if (i + j) % 2 == 0:
                s.append(c)
            else:
                s.append(d)
        uk.append("".join(s))

    o = len(uk)

    gh = 0
    uo = 0
    for i in range(o):
        yu = uk[i]
        if len(yu) > gh:
            gh = len(yu)
            uo = i

    yk = 0
    yj = {}

    td = 0
    uk.sort()
    for i in range(len(uk) - 1):
        for j in range(i + 1, len(uk)):
            if len(uk[j]) < len(uk[i]):
                t = uk[j]
                uk[j] = uk[i]
                uk[i] = t
    for i in range(1, len(uk)):
        j = i
        while j >= 0:
            if uk[i].count(uk[j]) == 0:
                td = 1
            j = j - 1
    if td == 0:
        print('YES')
        for i in uk:
            print(i)
    else:
        print('NO')


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)