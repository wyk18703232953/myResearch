import random

def main(n: int) -> int:
    # 根据 n 生成测试数据，这里随机构造 k，范围 [1, 10 * n]，避免为 0
    if n <= 0:
        raise ValueError("n must be positive")
    k = random.randint(1, 10 * n)

    r_n = n * 2
    g_n = n * 5
    b_n = n * 8
    t = 0

    t += r_n // k
    if r_n % k != 0:
        t += 1

    t += g_n // k
    if g_n % k != 0:
        t += 1

    t += b_n // k
    if b_n % k != 0:
        t += 1

    print(t)
    return t

if __name__ == "__main__":
    # 示例：n = 10
    main(10)