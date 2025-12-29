import random

def query_factory(a_real, b_real):
    """
    构造一个本地 query 函数，用于模拟交互：
    返回 sign((a_real ^ c) - (b_real ^ d))
    """
    def query(c, d):
        val = (a_real ^ c) - (b_real ^ d)
        if val == 0:
            return 0
        return 1 if val > 0 else -1
    return query


def main(n):
    """
    n 作为规模参数，用于生成测试数据：
    - 随机生成 0 <= a_real, b_real < 2^n
    - 使用原算法逻辑恢复 a, b
    - 返回 (a, b, a_real, b_real)，便于检查正确性
    """
    # 限定 n 的比特位数
    max_bits = n
    if max_bits <= 0:
        max_bits = 1
    if max_bits > 30:
        max_bits = 30

    # 生成测试数据
    upper = 1 << max_bits
    a_real = random.randrange(upper)
    b_real = random.randrange(upper)

    # 构造本地 query
    query = query_factory(a_real, b_real)

    # 以下为原始程序逻辑，只改用本地 query，去除 input/print
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

    # 返回推断出的 (a, b) 以及真实值 (a_real, b_real)
    return a, b, a_real, b_real


# 示例：当作为脚本运行时，给一个固定规模测试
if __name__ == "__main__":
    n = 10
    a, b, a_real, b_real = main(n)
    print("Recovered a, b:", a, b)
    print("Real      a, b:", a_real, b_real)