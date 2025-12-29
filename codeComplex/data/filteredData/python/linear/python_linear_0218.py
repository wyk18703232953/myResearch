import random

def main(n):
    # 生成参数 a, b（根据需要可调整范围）
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)  # b 在原代码中未使用，但保留结构

    # 生成 n 行 (t, x, y)，原代码中实际只用到 x, y
    # 这里生成 t, x, y 都在一定范围内的随机整数
    data = []
    for _ in range(n):
        t = random.randint(0, 1)          # t 在原逻辑中用不到
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        data.append((t, x, y))

    c, d = {}, {}
    r = 0
    for _, x, y in data:
        i, j = a * x - y, (x, y)
        r += c.get(i, 0) - d.get(j, 0)
        c[i] = c.get(i, 0) + 1
        d[j] = d.get(j, 0) + 1

    # 输出结果
    print(2 * r)


if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)