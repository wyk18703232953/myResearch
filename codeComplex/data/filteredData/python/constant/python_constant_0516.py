import random


def main(n: int):
    # 生成测试数据（忽略 n，仅用于产生一组随机数据）
    # x, y, z ∈ [0, n]，t1, t2, t3 ∈ [1, n]（避免为 0）
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)
    t1 = random.randint(1, n if n > 0 else 1)
    t2 = random.randint(1, n if n > 0 else 1)
    t3 = random.randint(1, n if n > 0 else 1)

    a = abs(x - y) * t1
    b = abs(x - z) * t2 + abs(x - y) * t2 + t3 * 3

    if a < b:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    # 示例：可修改为任意规模
    main(10)