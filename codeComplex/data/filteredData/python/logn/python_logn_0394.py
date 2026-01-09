def main(n):
    # 原程序输入: n, k
    # 这里将 n 视为原程序中的 n
    # 并构造一个与 n 规模相关的确定性 k
    k = n * n + n // 2

    a, b, c = 0, k, 0

    while a < b:
        c = (a + b) // 2
        if c * n < k:
            a = c + 1

        else:
            b = c

    # 保持原程序输出行为
    # print(a)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值
    main(1000)