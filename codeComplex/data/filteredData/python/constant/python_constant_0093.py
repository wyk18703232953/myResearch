import random

def main(n):
    """
    n: 生成 n 组 (a, b) 测试数据并计算结果
    """
    # 生成测试数据：n 组随机正整数对 (a, b)
    # 可根据需要调整范围
    test_cases = []
    for _ in range(n):
        # 避免 0，取 [1, 10^6]
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)
        test_cases.append((a, b))

    # 对每组 (a, b) 执行原逻辑
    for a, b in test_cases:
        result = 0
        while min(a, b) != 0:
            x = max(a, b)
            y = min(a, b)
            a = x
            b = y
            result += a // b
            a %= b
        print(result)


# 示例：如需直接运行，取消下行注释并指定 n
# if __name__ == "__main__":
#     main(5)