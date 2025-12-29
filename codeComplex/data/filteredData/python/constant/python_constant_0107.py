import random

def operations(a, b):
    less = min(a, b)
    more = max(a, b)
    ops = 0
    while less > 0 and more > 0:
        ops += more // less
        more -= less * (more // less)
        less, more = more, less
    return ops

def main(n):
    # 生成 n 组测试数据 (a, b)，取值范围可根据需要调整
    test_cases = []
    for _ in range(n):
        # 保证 a, b 为正整数，避免除以 0
        a = random.randint(1, 10**9)
        b = random.randint(1, 10**9)
        test_cases.append((a, b))

    # 执行运算并输出结果
    for a, b in test_cases:
        print(operations(a, b))

if __name__ == "__main__":
    # 示例：调用 main，规模为 5
    main(5)