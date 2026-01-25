def main(n):
    # 根据 n 构造确定性输入规模
    # 原程序输入：
    # 第一行：n, s
    # 接下来 n 行：x, y
    # 这里我们令 s = n，构造 n 组时间点
    s = n

    h = []
    m = []
    l = []
    l.append(0)

    # 构造 n 组 (x, y)，确保是合法时间：0 <= x < 24, 0 <= y < 60
    # 使用简单算术生成确定性时间数据
    for i in range(n):
        x = (i * 3) % 24
        y = (i * 7) % 60
        h.append(x)
        m.append(y)
        l.append(x * 60 + y)

    if l[1] != 0 and (l[1] - l[0]) >= s + 1:
        print(0, 0)
    else:
        k = 2 * s + 2
        r = 0
        for i in range(n):
            if l[i + 1] - l[i] >= k:
                r = l[i] + s + 1
                break
            else:
                continue
        if r == 0:
            r = l[n] + s + 1
        print(r // 60, r % 60)


if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次运行
    main(10)