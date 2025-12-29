import random

def main(n):
    # 生成测试数据：
    # n 对 (a, b)，键 a 尽量有重复，b 为随机整数
    d = {}
    for _ in range(n):
        a = random.randint(1, n // 2 + 1)  # 增加重复概率
        b = random.randint(1, 100)
        d[a] = b

    # 生成 m 以及 m 对 (a, b) 更新数据
    m = max(1, n // 2)
    updates = []
    for _ in range(m):
        a = random.randint(1, n)          # 可能有新键，也可能更新旧键
        b = random.randint(1, 100)
        updates.append((a, b))

    # 按原逻辑执行
    for a, b in updates:
        if a in d and b > d[a]:
            d[a] = b
        elif a not in d:
            d[a] = b

    s = 0
    for i in d:
        s += d[i]
    print(s)


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)