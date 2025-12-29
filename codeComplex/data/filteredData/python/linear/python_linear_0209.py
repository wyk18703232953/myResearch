import random

def main(n):
    # 生成测试数据
    # 设定等待时间 s 在 0~30 分钟范围内
    s = random.randint(0, 30)

    # 生成 n 个随机到达时间，保证有序且在一天内（0~1439 分钟）
    times = sorted(random.sample(range(0, 24 * 60), n))

    # 原代码逻辑开始
    l = [0]
    for t in times:
        # t 已经是分钟数，这里模拟原始的 q,w 输入形式
        q, w = divmod(t, 60)
        q = q * 60 + w
        l.append(q)

    if l[1] - l[0] > s:
        print(0, 0)
        return

    for i in range(n):
        if l[i + 1] - l[i] > 2 * s + 1:
            l[i] += s + 1
            print(l[i] // 60, l[i] % 60)
            return

    l[-1] += s + 1
    print(l[-1] // 60, l[-1] % 60)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(5)