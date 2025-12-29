import random

def main(n):
    # 随机生成测试数据：
    # n: 元素个数
    # t: 在 [0, 10] 内随机
    # 每个元素生成 (x, m)，x, m 在 [0, 100] 内随机
    t = random.randint(0, 10)
    data = []
    for _ in range(n):
        x = random.randint(0, 100)
        m = random.randint(0, 100)
        data.append((x, m))

    # 原逻辑开始
    a = []
    for x, m in data:
        a.append((x - m / 2, m))
    a.sort()
    ans = 2
    for i in range(n - 1):
        x = a[i][0] + a[i][1] + t
        y = a[i + 1][0]
        ans += (x <= y) + (x < y)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)