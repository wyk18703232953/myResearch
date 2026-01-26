def main(n):
    """
    n: 问题规模，用来生成测试数据 (n_val, k_val)
    这里简单约定：
      n_val = n
      k_val = n // 2
    可根据需要修改生成规则。
    """
    m = 1000000007

    # 根据规模 n 生成测试数据
    n_val = n
    k_val = n // 2

    if n_val == 0:
        # print(0)
        pass
        return

    r = pow(2, k_val + 1, m) * n_val - pow(2, k_val, m) + 1
    # print(r % m)
    pass
if __name__ == "__main__":
    # 示例：用规模 n=10 运行
    main(10)