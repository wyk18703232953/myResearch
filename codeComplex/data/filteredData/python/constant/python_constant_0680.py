import random

def query_factory(secret_a, secret_b):
    """
    构造一个 query 函数，用于模拟交互：
    比较 (secret_a ^ secret_b) 与 (c ^ d) 的大小关系。
    返回：
      1  如果 (secret_a ^ secret_b) > (c ^ d)
      -1 如果 (secret_a ^ secret_b) < (c ^ d)
      0  如果相等
    """
    target = secret_a ^ secret_b

    def query(c, d):
        val = c ^ d
        if target > val:
            return 1
        elif target < val:
            return -1
        else:
            return 0

    return query


def main(n):
    """
    n 为规模参数，用于生成测试数据：
    - 在 [0, 2^n - 1] 范围内随机生成 secret_a, secret_b
    - 使用原算法逻辑恢复它们
    返回：(a, b, secret_a, secret_b)，其中 a, b 为算法还原结果
    """
    if n <= 0 or n > 30:
        raise ValueError("n 应在 1 到 30 之间")

    # 生成测试数据
    max_val = (1 << n) - 1
    secret_a = random.randint(0, max_val)
    secret_b = random.randint(0, max_val)

    query = query_factory(secret_a, secret_b)

    a = 0
    b = 0
    big = query(0, 0)

    for i in range(29, -1, -1):
        p = query(a ^ (1 << i), b)
        q = query(a, b ^ (1 << i))
        if p == q:
            if big == 1:
                a ^= 1 << i
            else:
                b ^= 1 << i
            big = p
        elif p == -1:
            a ^= 1 << i
            b ^= 1 << i

    # 返回推断出的 a, b 以及真实的 secret_a, secret_b 以便验证
    return a, b, secret_a, secret_b


if __name__ == "__main__":
    # 示例运行：n=5
    a, b, sa, sb = main(5)
    print("deduced a, b:", a, b)
    print("secret  a, b:", sa, sb)
    print("correct:", (a, b) == (sa, sb))