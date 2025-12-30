import random

def main(n):
    # n 作为规模参数，这里不直接参与计算，只用于控制数据范围
    # 你可以根据需要调整数据生成范围与 n 的关系
    max_coord = max(10, n)
    max_t = max(10, n)

    x = random.randint(-max_coord, max_coord)
    y = random.randint(-max_coord, max_coord)
    z = random.randint(-max_coord, max_coord)
    t1 = random.randint(1, max_t)
    t2 = random.randint(1, max_t)
    t3 = random.randint(1, max_t)

    if 3 * t3 + abs(x - z) * t2 + abs(x - y) * t2 <= abs(x - y) * t1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：使用规模 n = 100 运行一次
    main(100)