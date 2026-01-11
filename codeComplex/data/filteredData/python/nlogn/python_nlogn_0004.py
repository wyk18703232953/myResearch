def main(n):
    # n 表示原程序中的 n，t 也从 n 确定性生成
    # 这里设定 t = max(1, n // 3)，保证随规模增长
    t = max(1, n // 3)

    l = []
    for i in range(n):
        # 确定性生成 x 和 a，使区间有规律可控
        # x 随 i 线性增长，a 在 [1, 10] 内循环
        x = 3 * i
        a = (i % 10) + 1
        l.append((x - a / 2, x + a / 2))

    l.sort()
    res = 2
    for i in range(n - 1):
        diff = l[i + 1][0] - l[i][1]
        if diff == t:
            res += 1
        elif diff > t:
            res += 2

    # print(res)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 进行规模化实验
    main(10)