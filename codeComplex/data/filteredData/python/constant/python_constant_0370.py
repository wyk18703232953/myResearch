import random

def main(n):
    # 根据规模 n 生成测试数据 (a, b, c, n)
    # 这里将 a, b, c, n 控制在 1 到 n 的范围内
    a = random.randint(1, n)
    b = random.randint(1, n)
    c = random.randint(1, n)
    total_n = random.randint(1, n)

    if a < c or b < c:
        r = -1
    else:
        r = total_n - (a + b - c)

    print(-1 if r <= 0 else r)


if __name__ == '__main__':
    # 示例：使用规模 10 运行
    main(10)