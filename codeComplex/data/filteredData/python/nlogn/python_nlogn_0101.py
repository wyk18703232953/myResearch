import random

def main(n):
    # 生成测试数据
    # 约定：a, b, c 为整数，满足 1 <= c < n
    # d 为长度为 n 的整数数组
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, n - 1)  # 保证有 d[c-1] 和 d[c]

    d = [random.randint(1, 1000) for _ in range(n)]

    # 原逻辑
    d_sorted = sorted(d)
    e = d_sorted[c - 1]
    f = d_sorted[c]
    print(f - e)

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)