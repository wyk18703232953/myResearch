def permuteDigits(a, b):
    n = len(a)
    if len(a) < len(b):
        return a

    i = 0
    c = 0
    t = a[0]
    flag = 0
    lastind = []
    while i < len(a) and i < len(b) and a[i] >= b[i]:
        if c == n:
            i = i - 1
            t = a[i]
            a = a[:i] + a[i+1:]
            a.insert(lastind.pop(), t)
            flag = 1
            c = i
        elif (flag == 0 and a[c] == b[i]) or a[c] < b[i]:
            lastind.append(c)
            t = a[c]
            a = a[:c] + a[c+1:]
            a.insert(i, t)

        else:
            c = c + 1

        if a[i] < b[i]:
            break
        elif flag == 0 and a[i] == b[i]:
            i = i + 1
            c = i
    return a


def main(n):
    # 输入结构识别：
    # 原程序有两行字符串数字输入：aa, bb
    # 然后将 aa 每位拆为整数列表 a，bb 每位拆为整数列表 b
    # 这里将 n 映射为两个等长数字串的长度
    if n <= 0:
        return

    # 确定性生成长度为 n 的数字串 aa、bb
    # 使用简单算术构造，禁止任何随机性
    # aa: 递增模式（从 1 开始，对 10 取模）
    # bb: 递减模式（从 9 开始，对 10 取模）
    aa_digits = [(i % 10) for i in range(1, n + 1)]
    bb_digits = [((9 - i) % 10) for i in range(n)]

    # 转换为原程序中的 a, b
    a = aa_digits[:]
    b = bb_digits[:]

    # 原程序对 a 做降序排序
    a.sort(reverse=True)

    ans = permuteDigits(a, b)
    s = ""
    for x in ans:
        s += str(x)
    # print(int(s))
    pass
if __name__ == "__main__":
    # 示例：输入规模 n=8，对应于原注释中的 8 位数字示例
    main(8)