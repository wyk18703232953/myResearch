import random

def main(n):
    # 自动生成测试数据：
    # n 行，每行 2 个整数 (a[i][0], a[i][1])
    # 同时生成 k，1 <= k <= n
    random.seed(0)  # 固定随机种子，保证复现性

    k = random.randint(1, n)
    a = []
    for _ in range(n):
        # 这里可根据需要调整数据范围
        x0 = random.randint(0, 100)
        x1 = random.randint(0, 100)
        a.append([x0, x1])

    # 原逻辑
    a.sort(key=lambda x: x[1])
    a.sort(reverse=True, key=lambda x: x[0])
    b = a[k - 1]
    result = a.count(b)

    print("n =", n)
    print("k =", k)
    print("data:")
    for row in a:
        print(row)
    print("result:", result)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可按需要修改 n
    main(10)