def main(n):
    # n 表示字符串数量
    o = n
    uk = []
    gh = 0
    uo = 0

    # 确定性生成 o 个字符串，长度随 i 线性变化
    # 构造方式: 第 i 个字符串由字符 'a' + (i % 26) 重复 (i % (n+1) + 1) 次
    for i in range(o):
        length = (i % (n + 1)) + 1
        ch = chr(ord('a') + (i % 26))
        yu = ch * length
        if len(yu) > gh:
            gh = len(yu)
            uo = i
        uk.append(yu)

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
    main(10)