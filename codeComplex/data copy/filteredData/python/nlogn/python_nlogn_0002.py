def main(n):
    # 映射：n 为区间数量，t 固定为 5，区间端点由 n 确定性生成
    t = 5
    l = []
    for i in range(n):
        a = 2 * i + 3
        b = (i % 7) + 1
        x = a - b / 2
        y = a + b / 2
        l.append([x, y])

    l.sort()
    c = 0
    for i in range(n - 1):
        diff = l[i + 1][0] - l[i][1]
        if diff > t:
            c += 2
        elif diff == t:
            c += 1
    # print(c + 2)
    pass
if __name__ == "__main__":
    main(10)