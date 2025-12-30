import random

def main(n):
    # 生成测试数据：
    # a[i] = (x_i, t_i)
    # 约定：x_i 严格递增，t_i 为非负整数
    # 同时生成一个时间限制 t（与原代码中的 t 对应）
    a = []
    x = 0
    for _ in range(n):
        # 每次位置至少增加 1，至多增加 10
        x += random.randint(1, 10)
        # t_i 在 [0, 10] 范围内
        ti = random.randint(0, 10)
        a.append([x, ti])

    # 为了更贴近原始代码的逻辑，这里将 a 打乱再排序
    random.shuffle(a)
    a = sorted(a)

    # t 在 [0, 10] 范围内
    t = random.randint(0, 10)

    # 原始逻辑
    v = 2
    for i in range(n - 1):
        d = 2 * a[i + 1][0] - a[i + 1][1] - 2 * a[i][0] - a[i][1]
        if d > 2 * t:
            v += 2
        elif d == 2 * t:
            v += 1

    print(v)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)