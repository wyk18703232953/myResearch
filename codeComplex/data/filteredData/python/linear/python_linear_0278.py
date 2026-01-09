def main(n):
    # 解释原始输入结构：n, m, a, b 为四个整数
    # 在实验中，将参数 n 作为原程序中的第一个参数 n 的规模含义
    # 其余 m, a, b 由 n 确定性生成

    original_n = n
    m = n + 1 if n > 0 else 1
    a = (n % 5) + 1
    b = (n % 7) + 1

    if original_n % m == 0:
        # print(0)
        pass

    else:
        k = original_n % m
        # print(min(k * b, (m - k) * a))
        pass
if __name__ == "__main__":
    main(10)