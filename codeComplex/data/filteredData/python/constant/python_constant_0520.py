import random

def main(n: int):
    # 生成规模为 n 的测试数据：
    # 这里将 n 视为坐标与时间参数的最大绝对值范围
    # x, y, z ∈ [-n, n], t1, t2, t3 ∈ [1, n]
    x = random.randint(-n, n)
    y = random.randint(-n, n)
    z = random.randint(-n, n)
    t1 = random.randint(1, n if n > 0 else 1)
    t2 = random.randint(1, n if n > 0 else 1)
    t3 = random.randint(1, n if n > 0 else 1)

    d1 = abs(x - y) * t1
    d2 = abs(x - z) * t2 + abs(x - y) * t2 + 3 * t3
    if d2 <= d1:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：可修改 n 的大小进行测试
    main(10)