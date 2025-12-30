import random

def main(n, t=None, seed=0):
    random.seed(seed)

    # 生成测试数据：n 个区间 [x_i, x_i + len_i]，对应原程序中的 (center, length)
    # 为保持语义，生成中心 a[i][0] 和长度 a[i][1]
    a = []
    for _ in range(n):
        center = random.randint(0, 1000)
        length = random.randint(0, 1000)
        a.append([center, length])

    if t is None:
        t = random.randint(0, 1000)

    # 以下为原逻辑
    a = sorted(a)
    b = [a[i][0] - a[i][1] / 2 - a[i - 1][0] - a[i - 1][1] / 2 for i in range(1, n)]
    c = 2
    for i in range(n - 1):
        c += int(b[i] > t) * 2 + int(b[i] == t)

    print(c)


if __name__ == "__main__":
    # 示例调用：n=5，可根据需要修改 n 和 t
    main(5)