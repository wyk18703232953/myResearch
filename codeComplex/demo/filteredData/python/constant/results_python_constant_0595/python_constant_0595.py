def main(n):
    # 解释输入结构：
    # 原程序输入为两整数 n, k
    # 在重构中使用参数 n 作为原始的 n
    # 并设定 k 为 n 的简单确定性函数：k = n // 2 + 1（保证 k >= 1）
    orig_n = n
    k = n // 2 + 1

    r_n = orig_n * 2
    g_n = orig_n * 5
    b_n = orig_n * 8
    t = 0
    t += r_n // k
    if r_n % k != 0:
        t += 1
    t += g_n // k
    if g_n % k != 0:
        t += 1

    t += b_n // k
    if b_n % k != 0:
        t += 1
    # print(t)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的规模做时间复杂度实验
    main(10)