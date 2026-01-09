def main(n):
    # 解释输入结构：
    # 原程序：k, n, s, p = map(int, input().split())
    # 为了时间复杂度实验，将单个规模参数 n 映射为这四个参数
    #
    # 设：
    #   k = max(1, n // 3)
    #   n_pages = n
    #   s = max(1, n // 5)
    #   p = max(1, n // 7)
    #
    # 保证参数均为正整数，且随 n 线性变化，便于规模扩展
    
    k = max(1, n // 3)
    n_pages = n
    s = max(1, n // 5)
    p = max(1, n // 7)

    result = ((n_pages + s - 1) // s * k + p - 1) // p
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)