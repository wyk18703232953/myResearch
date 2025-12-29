import random

def main(n):
    # 生成第一组数据大小 m1，保证 1 <= m1 <= n
    m1 = max(1, n)

    d = {}
    # 第一组：生成 m1 行 (a, x)
    # a 在 [1, 2n] 范围内，x 在 [1, 100] 范围内
    for _ in range(m1):
        a = random.randint(1, 2 * n)
        x = random.randint(1, 100)
        d[a] = x

    # 生成第二组数据大小 m2，这里同样取 m2 = n
    m2 = n
    # 第二组：生成 m2 行 (b, y)
    for _ in range(m2):
        b = random.randint(1, 2 * n)
        y = random.randint(1, 100)
        d[b] = max(d.get(b, 0), y)

    print(sum(d.values()))


if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)