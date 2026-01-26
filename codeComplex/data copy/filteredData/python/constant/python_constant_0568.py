def main(n):
    # 对应原程序中的四个输入：n, m, k, l
    # 将规模 n 映射为原来的 n，其他参数用确定性方式构造
    N = n
    m = max(1, n // 3)
    k = n // 2
    l = n // 4

    x = (l + k) // m
    if x * m < l + k:
        x += 1
    assert x * m >= l + k

    if m * x > N:
        # print(-1)
        pass

    else:
        # print(x)
        pass
if __name__ == "__main__":
    main(10)