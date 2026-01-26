def main(n):
    # 生成两个只包含 0/1 的数字串，对应原程序中的两行输入
    # 将 n 映射为两行长度：len(a) = n，len(b) = 2n
    if n <= 0:
        # print(0)
        pass
        return

    len_a = n
    len_b = 2 * n

    # 确定性构造：使用简单的模运算生成 0/1 序列
    a = [(i % 2) for i in range(len_a)]
    b = [((i // 2) % 2) for i in range(len_b)]

    dff = len(b) - len(a)
    if dff < 0:
        # print(0)
        pass
        return

    lb = len(b)
    c = [0] * (lb + 1)
    for i in range(lb):
        c[i + 1] = c[i] + b[i]

    ans = 0
    for i in range(len(a)):
        item = a[i]
        if item:
            ans += (dff + 1 - (c[dff + i + 1] - c[i]))

        else:
            ans += (c[dff + i + 1] - c[i])

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小做复杂度实验
    main(5)