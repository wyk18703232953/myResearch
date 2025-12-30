import random

def main(n):
    # 生成测试数据：规模 n，对应原代码中的 n
    # 这里选择 m 与 n 同阶，例如 m = n，用于生成 m 组 (x, d)
    m = n

    # 预先计算与 n 无关的量
    a = (n * (n - 1)) // 2
    n2 = n // 2
    b = n2 * (n2 + 1)
    if n % 2 == 0:
        b -= n2

    s = 0

    # 生成测试数据并计算
    # x, d 可根据需求调整，这里简单取一个对称范围内的随机数
    for _ in range(m):
        x = random.randint(-10**3, 10**3)
        d = random.randint(-10**3, 10**3)
        s += x * n
        s += d * (a if d > 0 else b)

    print(s / n)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(10)