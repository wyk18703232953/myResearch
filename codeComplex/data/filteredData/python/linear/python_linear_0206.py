def main(n):
    # 解释输入结构（原程序）：
    # 第一行：n, s
    # 接下来 n 行：a, b（表示时间 a:b）
    #
    # 为了做时间复杂度实验，这里让参数 n 只控制“时间点数量”，
    # 而休息时间 s 设为与 n 有确定关系的值，使规模随 n 增长。
    #
    # 构造规则（完全确定性）：
    # - s = max(1, n // 3)
    # - 生成 n 个时间点 (a, b)，按分钟严格递增，且从 00:00 开始。
    #   第 j 个时间点对应从 0 开始计数的第 (j + 1) 分钟：
    #       total_minutes = j + 1
    #       a = total_minutes // 60
    #       b = total_minutes % 60
    #
    # 这样：
    # - 对于大部分 n，最早空档出现逻辑与原程序相同
    # - 数据规模和时间数量统一由 n 控制
    #
    # 如果想用不同的数据生成方式，只需保持 (n, s) 和 n 组 (a, b) 是确定的即可。
    s = max(1, n // 3)

    # 生成时间点列表 times，长度为 n，元素为 [a, b]
    # 第 j 个时间点为第 j + 1 分钟，确保从 00:01, 00:02, ... 开始递增
    times = []
    for j in range(n):
        total_minutes = j + 1
        a = total_minutes // 60
        b = total_minutes % 60
        times.append([a, b])

    # 以下是原程序的核心逻辑，只是将输入改为使用生成好的 times
    t = [[0, 0]]
    for j in range(n):
        a, b = times[j]
        total = a * 60 + b
        last = t[-1][0] * 60 + t[-1][1] + 1
        t.append([a, b])

        if j == 0:
            if total >= s + 1:
                print(0, 0)
                break

        if total - last > 2 * s:
            u = last + s
            print(u // 60, u % 60)
            break

        if j == n - 1:
            x = t[-1][0] * 60 + t[-1][1]
            print((x + s + 1) // 60, (x + s + 1) % 60)
            break


if __name__ == "__main__":
    # 示例调用：可以修改这里的 n 来改变“输入规模”
    main(10)