def main(n):
    # 解释 n 的映射：
    # n -> (n, m, k, l) 通过确定性方式构造
    # 为保证可规模化，将 m, k, l 定义为 n 的简单函数
    # 同时避免除以 0 的情况

    # n 作为原程序的 n
    original_n = max(1, n)

    # m 控制“每次增加量”，与 n 线性相关但不为 0
    m = max(1, n // 3 + 1)

    # k 和 l 作为目标值，随 n 线性增长
    k = n * 2 + 3
    l = n // 2 + 5

    cnt = (k + l + m - 1) // m
    if cnt * m > original_n:
        result = -1

    else:
        result = cnt

    # print(result)
    pass
if __name__ == "__main__":
    main(10)