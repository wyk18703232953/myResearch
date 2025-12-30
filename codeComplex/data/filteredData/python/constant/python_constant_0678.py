import random

def hidden_function(x, y, A, B):
    """模拟交互：返回 sign((A ^ x) - (B ^ y))，为 {-1, 0, 1}."""
    val = (A ^ x) - (B ^ y)
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0

def main(n=30):
    """
    将原交互式程序改为非交互版本。
    n 为使用的二进制位数（最高位为 n-1，最低位为 0）。
    内部随机生成 A, B，并用算法还原它们。
    返回 (a, b, A, B)，其中 a, b 为推断结果，A, B 为真实值。
    """
    # 1. 生成测试数据（隐藏的 A, B）
    # A, B 限制在 n 位以内
    max_val = (1 << n) - 1
    A = random.randint(0, max_val)
    B = random.randint(0, max_val)

    # 2. 用原算法的逻辑来“询问” hidden_function
    # 初始询问：'?', 0, 0
    t = hidden_function(0, 0, A, B)

    # s 数组长度按原代码使用到 0..30 共 31 个元素，这里按 n 位扩展
    s = [0] * (n + 1)  # s[n] 用作最高位的标志，依次推到 s[0]
    if t == 1:
        s[n] = 1
    else:
        s[n] = -1

    a = 0
    b = 0
    # 原代码是 range(30, 0, -1)，即从最高位 30 -> 1
    for i in range(n, 0, -1):
        # 询问 (a + 2^(i-1), b)
        c = (1 << (i - 1)) + a
        d = b
        ans1 = hidden_function(c, d, A, B)

        # 询问 (a, b + 2^(i-1))
        c = a
        d = (1 << (i - 1)) + b
        ans2 = hidden_function(c, d, A, B)

        if ans1 == -1 and ans2 == 1:
            a += 1 << (i - 1)
            b += 1 << (i - 1)
            s[i - 1] = s[i]
        elif ans1 == 1 and ans2 == -1:
            # 原代码中 a += 0 << (i-1), b += 0 << (i-1) 实际不变
            s[i - 1] = s[i]
        else:
            s[i - 1] = ans1
            if s[i] == 1:
                a += 1 << (i - 1)
                # b 不变
            else:
                # a 不变
                b += 1 << (i - 1)

    # 原代码: print('!', a, b)
    # 这里返回结果，同时可用于测试正确性
    return a, b, A, B

if __name__ == "__main__":
    # 示例运行，默认 n=30
    a, b, A, B = main(30)
    print("Predicted:", a, b)
    print("Actual   :", A, B)