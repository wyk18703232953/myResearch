import random

def main(n):
    # 生成测试数据：m 条 (x, d)
    # 这里设置 m 与 n 同规模，也可按需调整
    m = n
    # x 在 [-10^3, 10^3]，d 在 [-10^3, 10^3] 范围内随机生成
    test_data = [(random.randint(-1000, 1000), random.randint(-1000, 1000)) for _ in range(m)]

    res = 0
    mx = (n - 1) * n // 2
    if n & 1:
        mn = (n // 2) * (n // 2 + 1)
    else:
        mn = n * n // 4

    for x, d in test_data:
        res += x * n
        if d > 0:
            res += mx * d
        else:
            res += mn * d

    print(f"{res / n:.10f}")

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)