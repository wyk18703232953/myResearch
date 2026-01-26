def Sort(x):
    if len(x) == 1:
        return x

    a = Sort(x[:len(x) // 2])
    b = Sort(x[len(x) // 2:])

    c = []
    i = 0
    j = 0
    while (i < len(a)) and (j < len(b)):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1

        else:
            c.append(b[j])
            j += 1

    c = c + b[j:]
    c = c + a[i:]

    return c


def main(n):
    # 生成确定性输入：
    # 原程序结构：
    #   第一行: 任意输入（被丢弃）
    #   第二行: 一行整数，形成列表 m
    # 这里用 n 表示列表 m 的长度
    # 列表内容：一个简单的确定性排列，包含重复和无序性
    m = [(i * 3 + 7) % (n + 5) for i in range(n)]

    newm = Sort(m)
    count = 0
    for i in range(len(m)):
        if newm[i] != m[i]:
            count += 1

    if count / 2 <= 1:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)