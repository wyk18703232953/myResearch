import random

def main(n):
    """
    n: 规模参数，这里理解为测试数据组数 q
    """
    q = n  # 直接用 n 作为原程序中的 q
    otvet = []
    tests = []

    # 根据 n 生成测试数据 (n 组 (n, m, k))
    # 可以根据需要调整生成范围
    for _ in range(q):
        # 生成可能为负的 n, m，和非负的 k
        ni = random.randint(-10**6, 10**6)
        mi = random.randint(-10**6, 10**6)
        ki = random.randint(0, 10**6)
        tests.append((ni, mi, ki))

    # 原逻辑封装
    for ni, mi, ki in tests:
        n_abs = -ni if ni < 0 else ni
        m_abs = -mi if mi < 0 else mi

        if m_abs > ki or n_abs > ki:
            otvet.append(-1)
        elif m_abs % 2 == ki % 2 and n_abs % 2 == ki % 2:
            otvet.append(ki)
        elif m_abs % 2 == ki % 2 or n_abs % 2 == ki % 2:
            otvet.append(ki - 1)
        else:
            otvet.append(ki - 2)

    # 输出结果
    for ans in otvet:
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5) 生成 5 组随机测试并输出结果
    main(5)