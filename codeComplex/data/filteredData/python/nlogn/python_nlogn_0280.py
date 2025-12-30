import random

def main(n):
    # 生成测试数据：
    # 第一部分：n 个 (a, b) 对
    # 第二部分：m 个 (x, y) 对，这里令 m = n，可根据需要调整
    pairs1 = []
    pairs2 = []

    # 为了简单，键和值都在 1..2n 范围内
    for _ in range(n):
        a = random.randint(1, 2 * n)
        b = random.randint(1, 2 * n)
        pairs1.append((a, b))

    m = n
    for _ in range(m):
        x = random.randint(1, 2 * n)
        y = random.randint(1, 2 * n)
        pairs2.append((x, y))

    # 原始逻辑
    d = {}
    for a, b in pairs1:
        d[a] = b

    s = 0
    for x, y in pairs2:
        if x in d:
            d[x] = max(d[x], y)
        else:
            d[x] = y

    for i in d:
        s += d[i]

    print(s)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)