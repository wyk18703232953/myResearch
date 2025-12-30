import random

def main(n):
    # 生成测试数据：
    # 在 [0, 2^n - 1] 范围内随机生成两个整数 l, r
    if n <= 0:
        return 0  # 规模无效时返回 0

    max_val = (1 << n) - 1
    l = random.randint(0, max_val)
    r = random.randint(0, max_val)

    # 原始逻辑
    p = l ^ r
    x = 1
    while x <= p:
        x = x << 1
    result = x - 1

    print(result)
    return result

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)