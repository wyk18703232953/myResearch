import random

def main(n: int):
    # 生成测试数据：n 为较大的数，m 为 1..n 之间的随机数
    # 确保 m != 0
    if n <= 1:
        n_val, m_val = 1, 1
    else:
        n_val = n
        m_val = random.randint(1, n)

    a = 0
    while m_val:
        a += n_val // m_val
        n_val, m_val = m_val, n_val % m_val
    print(a)


if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)