def main(n):
    # 这里根据 n 生成测试数据：
    # 设 m 与 n 同规模，这里简单取 m = n
    m = n

    s = 0
    e = n - 1
    for i in range(n // 2):
        for j in range(m):
            # print(s + 1, j + 1)
            pass
            # print(e + 1, m - j)
            pass
        s += 1
        e -= 1

    if n % 2 == 1:
        s = n // 2
        for j in range(m // 2):
            # print(s + 1, j + 1)
            pass
            # print(s + 1, m - j)
            pass
        if m % 2 == 1:
            # print(s + 1, m // 2 + 1)
            pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)