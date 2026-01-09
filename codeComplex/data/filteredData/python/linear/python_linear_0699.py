def main(n):
    # 解释原输入结构：
    # 原程序读取两个整数 n, v
    # 我们将实验规模参数映射为：
    #   n -> 原程序的 n
    #   v -> 一个与 n 相关、确定性的值
    #
    # 这里选择 v = n // 2 + 1，保证对不同 n 有可扩展性，且完全确定
    v = n // 2 + 1

    res = 0
    cur_tank = 0
    for c in range(1, n + 1):
        need_to_by = min(v - cur_tank, n - c - cur_tank)
        res += need_to_by * c
        cur_tank += need_to_by
        cur_tank -= 1
    # print(res)
    pass
if __name__ == "__main__":
    main(10)