def main(n):
    # 输入规模映射：
    # 原程序：第一行 n 表示点对数量，其后 n 行每行两个整数 x, y
    # 这里：使用 n 作为点对数量，确定性生成 (x, y)
    # 生成规则（完全确定性）：
    #   x = i
    #   y = i // 2
    # 对于 i in [0, n-1]
    l = []
    for i in range(n):
        x = i
        y = i // 2
        l.append((x + y, x - y))

    l.sort()
    r = -2000000000
    a = 0
    for u in l:
        if u[1] >= r:
            a += 1
            r = u[0]
    # print(a)
    pass
if __name__ == "__main__":
    main(10)