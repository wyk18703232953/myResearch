def main(n):
    # 映射：n -> 点的数量 n_points，t 固定为 1
    if n <= 0:
        return
    n_points = n
    t = 1

    intervals = []
    # 生成确定性 (x, a)，例如：
    # x = i * 3
    # a = (i % 5) * 2 + 1  -> 保证 a 为奇数，可产生非整数端点
    for i in range(n_points):
        x = i * 3
        a = (i % 5) * 2 + 1
        left = x - a / 2
        right = x + a / 2
        intervals.append((left, right))

    intervals.sort()
    ans = 2
    for i in range(n_points - 1):
        dis = intervals[i + 1][0] - intervals[i][1]
        if dis > t:
            ans += 2
        elif dis == t:
            ans += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)