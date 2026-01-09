def main(n):
    # 根据规模 n 生成测试数据：
    # 原题 main 读取的是两个整数 n, m，这里为了演示，
    # 我们令 m = n（生成 n x n 的棋盘规模）。
    m = n

    s, e, ans = [1, 1], [n, m], []
    # 按原逻辑生成坐标对
    for _ in range(n * m // 2):
        ans.append(s[:])
        ans.append(e[:])
        s[1], e[1] = s[1] + 1, e[1] - 1
        if s[1] == m + 1:
            s = [s[0] + 1, 1]
        if not e[1]:
            e = [e[0] - 1, m]
    if (n * m) & 1:
        ans.append([s[0], s[1]])

    # 输出结果
    for i in ans:
        # print(*i)
        pass
if __name__ == "__main__":
    # 示例：调用 main(3) 生成 3x3 棋盘的测试输出
    main(3)