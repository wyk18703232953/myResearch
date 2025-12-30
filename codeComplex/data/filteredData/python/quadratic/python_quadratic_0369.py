def main(n):
    import random

    # 生成一个 h x w 的随机网格，n 作为规模参数
    # 这里简单地取 h = w = max(1, n)，你可以根据需要修改生成规则
    h = max(1, n)
    w = max(1, n)

    # 随机生成星号网格，'*' 或 '.'，星号概率可按需要调整
    p_star = 0.4
    rng = random.Random(0)  # 固定种子以便复现
    grid = []
    for _ in range(h):
        row = []
        for _ in range(w):
            row.append('*' if rng.random() < p_star else '.')
        grid.append("".join(row))

    # 原程序逻辑开始（去掉 input，改用上面生成的 h, w, grid）
    s = [list("." * (w + 2))]
    for row in grid:
        s.append(list("." + row + "."))
    s.append(list("." * (w + 2)))

    b = [[0] * (w + 2) for _ in range(h + 2)]
    c = [[0] * (w + 2) for _ in range(h + 2)]

    # 向下、向右累积
    for i in range(1, h + 2):
        for j in range(1, w + 2):
            if s[i][j] == "*":
                b[i][j] = b[i - 1][j] + 1
                c[i][j] = c[i][j - 1] + 1

    # 向上、向左修正为最小臂长
    for i in range(h, -1, -1):
        for j in range(w, -1, -1):
            if s[i][j] == "*":
                b[i][j] = min(b[i][j], b[i + 1][j] + 1)
                c[i][j] = min(c[i][j], c[i][j + 1] + 1)

    ans = []
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            t = min(b[i][j], c[i][j]) - 1
            if t > 0:
                ans.append((i, j, t))

    # 差分数组重建验证
    b = [[0] * (w + 2) for _ in range(h + 2)]
    c = [[0] * (w + 2) for _ in range(h + 2)]

    for i, j, t in ans:
        b[i - t][j] += 1
        b[i + t + 1][j] -= 1
        c[i][j - t] += 1
        c[i][j + t + 1] -= 1

    for i in range(h + 1):
        for j in range(w + 1):
            b[i + 1][j] += b[i][j]
            c[i][j + 1] += c[i][j]
            if i != 0 and j != 0:
                if (b[i][j] + c[i][j] > 0) != (s[i][j] == "*"):
                    print(-1)
                    return

    print(len(ans))
    for item in ans:
        print(*item)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)