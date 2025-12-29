import random

def main(n):
    # 生成测试数据
    # n：预约次数
    # m：需要的连续空闲时间长度（分钟）
    # 这里设定时间为一天内的分钟数 0~1439
    m = random.randint(1, 180)  # 随机 1~180 分钟
    times = sorted(random.sample(range(0, 24 * 60), n))  # n 个不重复时间点

    # 转换为原程序输入格式（小时, 分钟）
    schedule = [(t // 60, t % 60) for t in times]

    # 原有逻辑
    b = []
    d = []

    for x in range(n):
        a, c = schedule[x]
        if x == 0:
            if (a * 60) + c > m:
                b.append("0 0")
            d.append((a * 60) + c)
        else:
            if ((a * 60) + c) - d[-1] > (m * 2) + 1:
                f = d[-1] + m + 1
                b.append(str(f // 60) + " " + str((f % 60)))
            d.append((a * 60) + c)

    if len(b) == 0:
        f = d[-1] + m + 1
        b.append(str(f // 60) + " " + str((f % 60)))

    print(b[0])


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)