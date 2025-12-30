import random

def req_num(a, b, x, y, z):
    req_a = (x * 2) + y
    req_b = (z * 3) + y

    if (req_a - a) <= 0:
        ans_a = 0
    else:
        ans_a = req_a - a

    if (req_b - b) <= 0:
        ans_b = 0
    else:
        ans_b = req_b - b

    return ans_a + ans_b


def main(n):
    """
    使用规模 n 生成测试数据并计算结果。
    n 仅作为规模参数，不影响算法逻辑本身。
    这里示例：根据 n 控制随机数范围。
    """
    random.seed(0)

    # 根据 n 规模生成 a, b, x, y, z
    # 范围示例：0 ~ 10 * n
    a = random.randint(0, 10 * n)
    b = random.randint(0, 10 * n)
    x = random.randint(0, 10 * n)
    y = random.randint(0, 10 * n)
    z = random.randint(0, 10 * n)

    result = req_num(a, b, x, y, z)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)