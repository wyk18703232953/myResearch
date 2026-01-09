def main(n):
    # 确定性生成输入数据
    # 将 n 映射为原程序中的 n，a, b, c, t
    # 这里让 a, b, c, t 随 n 以确定性方式变化
    a = 2 + (n % 5)
    b = 1 + (n % 3)
    c = 1 + (n % 7)
    t = n + 5

    # 保证 l 中元素不大于 t，且随 n 增长
    l = [(i * 2) % (t + 1) for i in range(1, n + 1)]

    if c > b:
        r = 0
        for i in l:
            k = t - i
            k *= (c - b)
            r += k
        # print(a * n + r)
        pass

    else:
        # print(a * n)
        pass
if __name__ == "__main__":
    main(10)