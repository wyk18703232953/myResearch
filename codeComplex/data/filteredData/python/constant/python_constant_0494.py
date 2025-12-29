import random

def main(n):
    # 生成 n 组测试数据
    test_data = []
    for _ in range(n):
        # 随机生成 x, y, k，可根据需要调整数据范围
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        k = random.randint(0, 10**6)
        test_data.append((x, y, k))

    # 模拟原逻辑并输出结果
    for x, y, k in test_data:
        # 原程序逻辑开始
        x, y = abs(x), abs(y)
        x, y = max(x, y), min(x, y)

        if (x % 2 != k % 2):
            k -= 1
            y -= 1

        if x > k:
            print(-1)
            continue

        if (x - y) % 2:
            k -= 1
            x -= 1

        print(k)

if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)