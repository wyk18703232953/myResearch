def main(n):
    # 这里根据 n 生成一个 s，作为测试数据。
    # 为了演示，设 s 为 n 的一半（向下取整），可以根据需要自行修改生成方式。
    s = n // 2

    a, b, c = 0, n + 1, 0

    while a < b:
        c = (a + b) // 2
        if c - sum(int(x) for x in str(c)) < s:
            a = c + 1

        else:
            b = c

    # 输出结果
    # print(n - b + 1)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10**6)
    main(10**6)