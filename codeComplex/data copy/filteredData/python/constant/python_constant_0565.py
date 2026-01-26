def main(n):
    # 解释输入结构：
    # 原程序需要四个整数 n, m, k, l
    # 这里将传入的 n 视为原始的 n
    # 其余 m, k, l 由 n 确定性构造
    original_n = n
    m = max(1, n // 2)
    k = n // 3
    l = n // 4

    n, m, k, l = original_n, m, k, l

    if m > n:
        # print(-1)
        pass
    elif l + k > n:
        # print(-1)
        pass

    else:
        s = (l + k) // m + bool((l + k) % m)
        if s * m > n:
            # print(-1)
            pass

        else:
            # print(s)
            pass
if __name__ == "__main__":
    main(1000000)