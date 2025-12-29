import random

def main(n):
    """
    n 作为规模参数，这里用于控制随机生成的两个整数的范围：
    0 <= a, b < 2^n
    """
    # 生成测试数据：两个非负整数 a, b
    upper = max(1, 2 ** n)
    a = random.randrange(upper)
    b = random.randrange(upper)

    # 原逻辑开始
    l1 = a
    l2 = b

    x = l1 ^ l2
    y = 1
    while y <= x:
        y = y * 2

    print(y - 1)

if __name__ == "__main__":
    # 示例：使用 n=10 运行一次
    main(10)