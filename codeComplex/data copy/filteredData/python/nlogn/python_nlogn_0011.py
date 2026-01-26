def main(n):
    # 解释：将 n 映射为原程序中的 n，t 为一个确定性的值
    # 输入结构：第一行 n, t；接着 n 行，每行两个整数
    # 这里 t 固定为 n // 2，a[i] 由简单算术构造得到
    t = n // 2

    # 构造 a：n 行，每行两个整数 [x, y]
    # 原程序会对 a 排序，这里也保留这一行为
    # 使用确定性构造：a[i] = [i, (i * 3) % (n + 1) + 1]
    a = [[i, (i * 3) % (n + 1) + 1] for i in range(n)]
    a = sorted(a)

    if n <= 1:
        # 对于 n <= 1，原程序中 b 和循环都为空，c 从 2 开始保持不变
        c = 2
        # print(c)
        pass
        return

    b = [a[i][0] - a[i][1] / 2 - a[i - 1][0] - a[i - 1][1] / 2 for i in range(1, n)]
    c = 2
    for i in range(n - 1):
        c += int(b[i] > t) * 2 + int(b[i] == t)
    # print(c)
    pass
if __name__ == "__main__":
    # 示例：以 n = 10 作为输入规模运行一次
    main(10)