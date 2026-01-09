def main(n):
    # 生成确定性输入数据：列表 m，长度为 n
    # 使用简单的算术序列作为数据：m[i] = (i * 2) % (n + 3)
    m = [(i * 2) % (n + 3) for i in range(n)]

    t = []
    for i in range(n):
        if i == 0:
            t.append(m[i] + 1)

        else:
            t.append(max(t[i - 1], m[i] + 1))
    if n == 0:
        s = 0

    else:
        s = t[n - 1] - m[n - 1] - 1
        for i in range(n - 2, -1, -1):
            if t[i] < t[i + 1] - 1:
                t[i] = t[i + 1] - 1
            s += t[i] - m[i] - 1
    # print(s)
    pass
if __name__ == "__main__":
    main(10)