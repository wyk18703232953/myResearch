def main(n):
    # 映射输入结构：
    # 第一行：a b
    # 第二行：d 列表，长度为 n，范围在 (0, b) 且递增
    if n <= 0:
        return

    a = 0
    b = n * 10

    # 构造一个严格递增且在 (a, b) 内的序列 d
    # 使用等差递增，保证确定性
    step = max(1, b // (n + 1))
    d = [step * (i + 1) for i in range(n)]
    d = [min(x, b - 1) for x in d]

    e = []
    e1 = []
    mx = 0
    current = 0
    for i in range(len(d)):
        if i % 2 == 0:
            e.append(d[i] - current)

        else:
            e1.append(d[i] - current)
        current = d[i]
    if i % 2 == 0:
        e1.append(b - current)

    else:
        e.append(b - current)
    mx = sum(e)
    su = 0
    su2 = sum(e1)
    for i in range(len(e)):
        su += e[i]
        mx = max(mx, su + su2 - 1)
        try:
            su2 -= e1[i]
        except:
            break
    # print(mx)
    pass
if __name__ == "__main__":
    main(10)