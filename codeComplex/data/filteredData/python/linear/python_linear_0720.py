import random

def main(n):
    # 生成测试数据
    # n 为 b 的规模；令 m 也为 n，便于构造
    m = n

    # 生成 b 和 g，保证为非负整数，范围可自行调整
    # 这里取 [0, 100] 的随机整数
    b = [random.randint(0, 100) for _ in range(n)]
    g = [random.randint(0, 100) for _ in range(m)]

    # 原逻辑开始
    first_max = 0
    second_max = 0
    for i in range(n):
        if b[i] < first_max and b[i] > second_max:
            second_max = b[i]
        if b[i] >= first_max:
            second_max = first_max
            first_max = b[i]

    first_min = min(g)

    if first_max > first_min:
        print(-1)
    else:
        total = sum(b) * m + sum(g) - m * first_max + (first_max - second_max) * (first_min != first_max)
        print(total)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)