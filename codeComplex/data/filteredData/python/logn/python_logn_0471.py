from sys import stdout

def judge(x, y, A, B):
    """
    模拟交互裁判：
    若 A > B: 返回 1
    若 A < B: 返回 -1
    若 A == B: 返回 0
    这里的原题逻辑通常是比较 (A ^ x) 与 (B ^ y)。
    根据经典交互题（如 CF 739D）的设定：
    返回：
      -1 如果 (A ^ x) < (B ^ y)
       0 如果 (A ^ x) == (B ^ y)
       1 如果 (A ^ x) > (B ^ y)
    """
    va = A ^ x
    vb = B ^ y
    if va < vb:
        return -1
    elif va > vb:
        return 1
    else:
        return 0


def solve_with_judge(m, A, B):
    """
    使用与原交互逻辑等价的算法恢复 A, B。
    m 为位数上限（原代码固定为 30）。
    """
    a, b = 0, 0
    fle = 1
    # 初次比较 (0,0)
    if fle:
        resp1 = judge(a, b, A, B)
        fle = 0
    for i in range(m):
        # 询问 (a + 2^(m-1-i), b + 2^(m-1-i))
        resp2 = judge(a + 2 ** (m - 1 - i), b + 2 ** (m - 1 - i), A, B)
        if resp1 == -1 and resp2 == 1:
            # 说明当前位 B 有 1
            b += 2 ** (m - 1 - i)
            fle = 1
        elif resp1 == 1 and resp2 == -1:
            # 说明当前位 A 有 1
            a += 2 ** (m - 1 - i)
            fle = 1
        else:
            # 此位两者相同或者都为 0/1，需要再问一次
            fle = 0
            resp3 = judge(a + 2 ** (m - 1 - i), b, A, B)
            if resp3 == -1:
                # 说明 (A^a') < (B^b) ，根据推导这一位两者皆为 1
                b += 2 ** (m - 1 - i)
                a += 2 ** (m - 1 - i)
        # 如果本轮确定了某一边有 1，则需要重新获取 resp1
        if fle:
            resp1 = judge(a, b, A, B)
            fle = 0
    return a, b


def main(n):
    """
    n 为规模参数，用于生成测试数据：

    这里采用：
      - 使用 n 作为位数上限 m（若 n>30，可以取 m = min(n, 30) 或直接使用 n）
      - 随机或固定生成 A, B 在 [0, 2^m) 内
    为了可复现，这里采用简单生成方式：
      A = 2^(m-1) - 1
      B = 2^(m-1) - 2
    你也可以改成随机数生成。
    """
    import random

    # 设置位数上限
    m = n if n > 0 else 1
    # 可按需求裁剪位数，比如原题固定 30 位，可写： m = min(n, 30)
    m = min(m, 30)

    # 生成测试数据 A, B（在 [0, 2^m) 内）
    # 这里使用随机生成，便于测试不同情况
    max_val = (1 << m) - 1
    A = random.randint(0, max_val)
    B = random.randint(0, max_val)

    # 运行算法推断 a, b
    a, b = solve_with_judge(m, A, B)

    # 输出结果与真实值，用于验证
    print("m =", m)
    print("True A, B:", A, B)
    print("Recovered a, b:", a, b)
    print("Check A==a and B==b:", A == a and B == b)


if __name__ == "__main__":
    # 示例：使用 n = 30 运行
    main(30)