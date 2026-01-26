def main(n):
    """
    n: 规模参数，用于生成测试数据。
       在原题中需要输入 n, m，这里根据 n 生成：
       n_input = n
       m_input = n  (或任意依赖于 n 的规则，这里简单取 m = n)
    """
    # 生成测试数据（模拟原来的输入 n, m）
    n_input = n
    m_input = n  # 未实际使用，只是与原程序结构对齐

    # 原主逻辑开始（将原 main 中的代码改为使用 n_input, m_input）
    n_val, m_val = n_input, m_input

    x = ((n_val - 5) // 4 + ((n_val - 5) % 4 != 0))
    if n_val <= 5:
        a, b = '5', '5'

    else:
        a = '5' * (x + 1)
        b = '4' * x + '5'

    # 输出结果
    # print(a, b)
    pass
if __name__ == '__main__':
    # 示例：调用 main(10) 进行测试
    main(10)