import random

def main(n: int):
    # 生成测试数据：整数 s，以及 n 对 (x, y)
    # 这里假设时间范围在一天内 [0:00, 23:59]
    # s 随机生成在 [0, 120] 分钟内
    s = random.randint(0, 120)

    h = []
    m = []
    l = [0]

    # 生成 n 个时间点（小时、分钟），保证有序且在一天内
    # 先生成 n 个分钟数并排序
    times = sorted(random.randint(0, 23 * 60 + 59) for _ in range(n))
    for t in times:
        x = t // 60
        y = t % 60
        h.append(x)
        m.append(y)
        l.append(t)

    # 以下为原逻辑
    if l[1] != 0 and (l[1] - l[0]) >= s + 1:
        print(0, 0)
    else:
        k = 2 * s + 2
        r = 0
        for i in range(n):
            if l[i + 1] - l[i] >= k:
                r = l[i] + s + 1
                break
        if r == 0:
            r = l[n] + s + 1
        print(r // 60, r % 60)


# 示例：调用 main(5)
if __name__ == "__main__":
    main(5)