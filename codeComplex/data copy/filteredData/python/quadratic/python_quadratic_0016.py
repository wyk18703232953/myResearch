def main(n):
    # 映射：n 为点的个数，半径 r 取固定值 n//2+1 保证有意义
    if n <= 0:
        return
    r = max(1, n // 2 + 1)
    # 生成确定性的坐标：间隔为 r//2+1，避免太密集
    step = r // 2 + 1
    x_coord = [i * step for i in range(n)]

    d = {}
    res = []
    for i in x_coord:
        final = r
        for j in range(i - r, i + r + 1):
            check = d.get(j, [-1, -1])
            if check[0] > 0:
                potential = check[1] + ((4 * r * r) - ((i - check[0]) ** 2)) ** 0.5
                final = max(potential, final)
        for j in range(i - r, i + r + 1):
            d[j] = (i, final)
        res.append(final)
    # 与原程序行为一致：在一行输出，用空格分隔
    # print(" ".join(str(x) for x in res))
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以做规模实验
    main(5)