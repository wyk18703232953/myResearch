import random


def main(n: int):
    # 生成规模为 n 的测试数据 v，模拟原本通过 input() 读入的点
    # 这里生成 [-10^6, 10^6] 范围内的整数坐标
    v = []
    a = list(range(n))
    for _ in range(n):
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        v.append([x, y, x * x + y * y])

    # 原逻辑：不断随机打乱顺序，寻找一组 +/- 使得最终向量长度满足限制
    while True:
        x = 0
        y = 0
        ans = [0] * n
        random.shuffle(a)
        for i in range(n):
            vx, vy = v[a[i]][0], v[a[i]][1]
            # 比较加上和减去该向量后模长的平方
            if (x + vx) ** 2 + (y + vy) ** 2 <= (x - vx) ** 2 + (y - vy) ** 2:
                x += vx
                y += vy
                ans[a[i]] = 1
            else:
                x -= vx
                y -= vy
                ans[a[i]] = -1
        if x * x + y * y <= 1500000 ** 2:
            print(*ans)
            break


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)