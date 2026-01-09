def main(n):
    # 在原程序中，有两个输入：n 和 m
    # 这里将规模参数 n 作为“第一个输入”的值
    # 为了可规模化和确定性，构造第二个输入 m 为 n 的某个确定性函数
    # 例如：m = n * (n + 1)，保证随 n 增长
    if n <= 0:
        return 0
    first = n
    second = n * (n + 1)
    m = second
    n_val = first
    result = m // n_val + (1 if m % n_val else 0)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)