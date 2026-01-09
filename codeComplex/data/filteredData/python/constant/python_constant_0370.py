def main(n):
    # 解释输入结构：
    # 原程序：a, b, c, n = P()   （一次读取 4 个整数）
    # 现将 n 映射为原程序的第四个输入参数 n_input
    # 并用确定性方式生成 a, b, c
    a = n + 1
    b = 2 * n + 3
    c = n

    if a < c or b < c:
        r = -1

    else:
        r = n - (a + b - c)
    # print(-1 if r <= 0 else r)
    pass
if __name__ == "__main__":
    main(10)