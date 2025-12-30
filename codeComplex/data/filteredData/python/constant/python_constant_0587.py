import random

def main(n: int):
    # 生成测试数据：x, y 在 [1, n] 内随机取值
    # 保证 x, y 为整数，范围可按需求调整
    x = random.randint(1, n)
    y = random.randint(1, n)

    a = 1 + 1
    b = n + n
    c = x + y
    distance_w = c - a
    distance_b = b - c

    if distance_w <= distance_b:
        result = 'White'
    else:
        result = 'Black'

    print(result)
    return result

if __name__ == "__main__":
    # 示例：可修改 n 测试不同规模
    main(10)