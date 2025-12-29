import random

def main(n):
    # 生成测试数据：
    # 第一组有 n 个键值对，第二组也有 n 个键值对
    # 键在 1..2n 之间，值在 1..100 之间
    k = {}
    s = 0

    # 第一组数据
    for _ in range(n):
        a = random.randint(1, 2 * n)
        x = random.randint(1, 100)
        k[a] = x

    # 第二组数据
    for _ in range(n):
        b = random.randint(1, 2 * n)
        y = random.randint(1, 100)
        if b in k:
            k[b] = max(k[b], y)
        else:
            k[b] = y

    s = 0
    for h in k.values():
        s += h

    print(s)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)