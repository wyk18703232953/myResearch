import random

def main(n):
    # 生成测试数据：n 个二维向量，坐标在 [-10^6, 10^6] 范围内
    v = []
    for i in range(n):
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        v.append([x, y, i])

    # 模拟原始逻辑
    while True:
        random.shuffle(v)
        x = y = 0
        ans = [0] * n
        for i in range(n):
            if (x + v[i][0]) ** 2 + (y + v[i][1]) ** 2 < (x - v[i][0]) ** 2 + (y - v[i][1]) ** 2:
                x += v[i][0]
                y += v[i][1]
                ans[v[i][2]] = 1
            else:
                x -= v[i][0]
                y -= v[i][1]
                ans[v[i][2]] = -1
        if x * x + y * y <= 1500000 ** 2:
            print(*ans)
            break

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)