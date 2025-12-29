import random

def main(n):
    # 随机生成 m, a, b，规模受 n 影响
    # 保证 m >= 1
    m = random.randint(1, max(1, 2 * n))
    a = random.randint(1, max(1, 2 * n))
    b = random.randint(1, max(1, 2 * n))

    if n < m:
        result = min(a * (m - n), b * n)
    else:
        result = min(b * (n % m), a * (m - (n % m)))
    print(result)


if __name__ == "__main__":
    # 示例：可修改这里的参数测试不同规模
    main(10)