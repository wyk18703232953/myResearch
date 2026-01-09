def main(n):
    # 解释输入结构：
    # 原程序需要 N, M, K, L 四个整数
    # 这里用 n 确定性生成这四个值：
    # N 与规模线性相关，M、K、L 通过简单算术构造
    N = max(1, n)
    M = max(1, n // 2 + 1)
    K = n * 2
    L = n + (n // 3)

    each = (K + L) // M
    if (K + L) % M != 0:
        each += 1

    if each * M > N:
        result = -1

    else:
        result = each

    return result


if __name__ == "__main__":
    # 示例调用，使用一个固定的 n 以保证可重复性
    n = 10
    # print(main(n))
    pass