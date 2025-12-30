import random

def main(n):
    # 随机生成 m, a, b，满足题意：m > 0
    if n <= 0:
        print(0)
        return

    m = random.randint(1, max(1, n * 2))
    a = random.randint(1, 10**6)
    b = random.randint(1, 10**6)

    # 原逻辑
    z = (n % m) * b
    x = ((n // m + 1) * m - n) * a
    y = min(z, x)
    print(y if y > 0 else 0)

if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(100)