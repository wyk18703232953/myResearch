import random


def main(n: int):
    # 1. 生成测试数据：n 个二维向量 (x, y)
    # 可根据需要调整数据规模范围
    v = []
    for i in range(n):
        # 生成 -10^6 到 10^6 的随机整数作为向量坐标
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        v.append([x, y, i])

    # 2. 保持原始逻辑：不断随机打乱顺序，尝试找到满足长度限制的符号分配
    LIMIT = 1500000
    while True:
        random.shuffle(v)
        x = y = 0
        ans = [0] * n
        for i in range(n):
            # 尝试 +v[i]
            if (x + v[i][0]) ** 2 + (y + v[i][1]) ** 2 < (x - v[i][0]) ** 2 + (y - v[i][1]) ** 2:
                x += v[i][0]
                y += v[i][1]
                ans[v[i][2]] = 1
            else:
                x -= v[i][0]
                y -= v[i][1]
                ans[v[i][2]] = -1
        if x * x + y * y <= LIMIT ** 2:
            print(*ans)
            break


if __name__ == "__main__":
    # 示例：n = 5，可按需修改
    main(5)