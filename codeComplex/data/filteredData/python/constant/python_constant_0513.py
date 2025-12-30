import random

def main(n):
    # 生成测试数据：
    # n 作为坐标/位置的上界，规模越大，坐标范围越大
    # x, y, z ∈ [0, n]
    # t1, t2, t3 ∈ [1, n]，保证时间系数为正
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)
    t1 = random.randint(1, n)
    t2 = random.randint(1, n)
    t3 = random.randint(1, n)

    ladder = abs(x - y) * t1
    elevator = abs(x - z) * t2 + 3 * t3 + abs(x - y) * t2

    if elevator > ladder:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的默认测试规模
    main(10)