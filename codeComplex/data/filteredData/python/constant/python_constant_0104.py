import random

def main(n):
    """
    n: 规模，即生成 n 组测试数据 (a, b)，并按原逻辑输出结果
    """
    c = []
    for _ in range(n):
        # 生成测试数据：避免 0，防止除零错误
        # 可根据需要调整范围
        a = random.randint(1, 10**4)
        b = random.randint(1, 10**4)

        a_curr = a
        b_curr = b
        z4 = 0

        while a_curr != 0 and b_curr != 0:
            z1 = z3 = 0
            if a_curr <= b_curr:
                z = b_curr / a_curr
                z1 = int(z)
                b_curr = b_curr - (z1 * a_curr)
            if b_curr <= a_curr and b_curr != 0:
                z2 = a_curr / b_curr
                z3 = int(z2)
                a_curr = a_curr - (z3 * b_curr)
            z4 = z4 + z1 + z3

        c.append(z4)

    for val in c:
        print(val)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)