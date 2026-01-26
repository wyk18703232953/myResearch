def main(n):
    # 映射：原程序中有两个输入 n, m
    # 这里将 n 作为“输入规模”，用于生成确定性的 (n_val, m_val)
    #
    # 生成规则（完全确定性）：
    #   n_val = n
    #   m_val = n^2 + 3n + 7
    n_val = n
    m_val = n * n + 3 * n + 7

    if n_val < 27:
        # 按原逻辑计算 m % 2**n
        result = m_val % (2 ** n_val)

    else:
        result = m_val

    return result


if __name__ == "__main__":
    # 示例调用：可按需修改 n 的值进行实验
    # print(main(10))
    pass