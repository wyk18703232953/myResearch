def main(n):
    # 将 n 映射为原程序的 n, m, k, l
    # 保证为正整数，且关系有一定扩展性
    a = max(1, n)
    b = max(1, n // 2)
    c = max(1, n // 3)
    d = max(1, n // 4)

    n_val = a
    m = b
    k = c
    l = d

    required = k + l
    per_friend = (required + m - 1) // m
    if m * per_friend > n_val:
        # print(-1)
        pass

    else:
        # print(per_friend)
        pass
if __name__ == "__main__":
    # 示例：以 10 作为规模参数调用
    main(10)