def main(n):
    """
    规模参数 n：用于生成测试数据。
    这里约定：令 s = n，用来驱动原逻辑的规模。
    如需其他关系，可自行修改 s 的生成方式。
    """
    # 根据规模 n 生成测试数据，这里简单设为 s = n
    s = n

    # 预处理 p 数组
    p = [0]
    for i in range(1, 19):
        p.append(p[-1] + 9 * (10 ** i - 1))

    choose = [0] * 19

    def find(curr_pos, max_pos, curr_s):
        if curr_pos == 0:
            return curr_s <= 0

        if curr_pos == max_pos:
            low = 1
        else:
            low = 0
        high = 9

        for d in range(low, high + 1):
            curr_val = d * (10 ** curr_pos - 1)
            if curr_val + p[curr_pos - 1] < curr_s:
                continue
            choose[curr_pos] = d
            return find(curr_pos - 1, max_pos, curr_s - curr_val)
        return False

    ans = n + 1
    for num_digit in range(1, 19):
        for i in range(1, num_digit + 1):
            choose[i] = 0
        if find(num_digit, num_digit, s):
            res = 0
            for i in range(num_digit, -1, -1):
                res = res * 10 + choose[i]
            ans = min(ans, res)
            break

    # 原程序输出 n - ans + 1
    print(n - ans + 1)


# 示例调用
if __name__ == "__main__":
    # 可根据需要修改规模 n
    main(100)