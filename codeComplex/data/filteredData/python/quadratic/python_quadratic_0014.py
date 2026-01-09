def main(n):
    # 生成测试数据：n 个x坐标，间隔为 r，使得有重叠
    r = 1
    xs = [i * r for i in range(n)]

    ys = []
    double_r_sq = (2 * r) ** 2
    for i in range(n):
        xi = xs[i]
        best = r  # 默认至少放在高度 r
        for j in range(i):
            dx = abs(xi - xs[j])
            if dx <= 2 * r:
                # 两圆相交时，上方圆心高度
                candidate = (double_r_sq - dx * dx) ** 0.5 + ys[j]
                if candidate > best:
                    best = candidate
        ys.append(best)

    # print(*ys)
    pass
if __name__ == "__main__":
    # 示例：规模为 5
    main(5)