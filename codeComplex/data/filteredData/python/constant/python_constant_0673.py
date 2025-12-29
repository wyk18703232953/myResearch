import random

def qu_factory(secret_a, secret_b):
    """
    构造查询函数 qu(a, b)，模拟交互：
    返回：
      1  如果 (a ^ secret_a) > (b ^ secret_b)
     -1  如果 (a ^ secret_a) < (b ^ secret_b)
      0  如果相等
    """
    def qu(a, b):
        va = a ^ secret_a
        vb = b ^ secret_b
        if va > vb:
            return 1
        elif va < vb:
            return -1
        else:
            return 0
    return qu

def main(n):
    """
    n 为规模，用作随机生成 secret_a, secret_b 的上界（2^n 以内）。
    返回 (a, b, secret_a, secret_b) 以便验证算法是否求对。
    """
    # 生成测试数据：在 [0, 2^n - 1] 范围内随机生成 secret_a, secret_b
    if n <= 0:
        n = 1
    upper = 1 << n
    secret_a = random.randrange(upper)
    secret_b = random.randrange(upper)

    qu = qu_factory(secret_a, secret_b)

    a = 0
    b = 0
    big = qu(a, b)

    for i in range(29, -1, -1):
        x = 1 << i
        f = qu(a + x, b)
        l = qu(a, b + x)
        if l == f:
            if big == 1:
                a += x
            else:
                b += x
            big = f
        elif f == -1:
            a += x
            b += x

    # 输出结果
    print("Found:", a, b)
    print("Secret:", secret_a, secret_b)
    return a, b, secret_a, secret_b

if __name__ == "__main__":
    # 示例：n=30，对应原算法处理的位数范围
    main(30)