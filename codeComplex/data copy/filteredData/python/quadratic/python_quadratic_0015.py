def main(n):
    # 确定性生成 r 和 x_coord
    # 让 r 随 n 增长，使区间范围有规模意义
    r = max(1, n // 5)
    x_coord = [(i * 3) % (10 * max(1, r)) for i in range(1, n + 1)]

    d = {}
    results = []
    for i in x_coord:
        final = r
        for j in range(i - r, i + r + 1):
            check = d.get(j, [-1, -1])
            if check[0] > 0:
                potential = check[1] + ((4 * r * r) - ((i - check[0]) ** 2)) ** 0.5
                final = max(potential, final)
        for j in range(i - r, i + r + 1):
            d[j] = (i, final)
        results.append(final)

    # 为了实验时保持输出行为，这里打印结果
    for value in results:
        # print(value)
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n
    main(10)