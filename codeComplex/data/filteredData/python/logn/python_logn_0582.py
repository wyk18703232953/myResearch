def main(n):
    # 生成测试数据：随机选择一个合法的 m，然后计算对应的 k
    # 为保证有解，先选 m，再反推 k
    if n <= 2:
        # 特殊情况下规模太小，直接处理
        # print(0)
        pass
        return

    # 这里简单选取 m 为 n//3（也可以换成其他策略或随机选）
    m_true = n // 3

    # 按原公式计算 k
    # S = ((n - m)^2 + n - 3m) / 2
    # k 就是这个 S
    k = ((n - m_true) ** 2 + n - 3 * m_true) // 2

    # 以下为原逻辑（去掉 input，使用上面生成的 n, k）
    l = 0
    r = n
    while True:
        m = (l + r) // 2
        S = ((n - m) ** 2 + n - 3 * m) // 2
        if S == k:
            # print(m)
            pass
            break
        elif S < k:
            r = m

        else:
            l = m


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要调整
    main(100)