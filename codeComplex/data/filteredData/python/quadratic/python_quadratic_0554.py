def main(n):
    # 在原程序中，输入是两个整数 n, m
    # 这里将 n 视为规模参数，并令 m = n，使规模为 n × n 的矩阵
    m = n

    s, e, ans = [1, 1], [n, m], []
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

    for i in ans:
        print(*i)


if __name__ == "__main__":
    # 示例调用：规模为 5（矩阵 5×5）
    main(5)