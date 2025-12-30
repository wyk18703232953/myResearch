import random

def num_ops(low, high):
    if high % low == 0:
        return high // low
    else:
        return (high // low) + num_ops(high % low, low)

def main(n):
    # 生成 n 组测试数据 (low, high)，保证 1 <= low <= high
    test_cases = []
    for _ in range(n):
        low = random.randint(1, 10**6)
        high = random.randint(low, 10**6 + low)  # 保证 high >= low
        test_cases.append((low, high))

    # 计算并输出每组测试数据的结果
    for low, high in test_cases:
        print(num_ops(low, high))

if __name__ == '__main__':
    # 示例：调用 main(5) 生成 5 组测试数据并运行
    main(5)