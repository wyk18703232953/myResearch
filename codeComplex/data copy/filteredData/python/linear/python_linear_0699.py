def main(n):
    # 解释输入结构：原程序需要两个整数 n, v
    # 这里将实验规模参数 n 映射为原程序中的 n，v 作为 n 的确定性函数
    orig_n = max(1, n)
    v = (orig_n // 2) + 1  # 一个与规模相关且确定性的值

    res = 0
    cur_tank = 0
    for c in range(1, orig_n + 1):
        need_to_by = min(v - cur_tank, orig_n - c - cur_tank)
        res += need_to_by * c
        cur_tank += need_to_by
        cur_tank -= 1
    # print(res)
    pass
if __name__ == "__main__":
    main(10)