def main(n):
    # 映射：给定规模 n，构造一对 (N, K)，均与 n 同阶，以便控制输入规模
    # 例如：N = n*n, K = n
    N = n * n
    K = n

    # 原始算法逻辑开始
    n_val = N - 1
    k_val = K - 1
    if n_val > (k_val * (k_val + 1)) // 2:
        result = -1

    else:
        l = -1
        r = k_val + 1
        while r > l + 1:
            m = (l + r) // 2
            if n_val > (m * (2 * k_val - m + 1)) // 2:
                l = m

            else:
                r = m
        result = r

    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值做规模实验
    main(1000)