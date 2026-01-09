def main(n):
    # 根据规模 n 生成测试数据：
    # 这里按原程序逻辑，s 的自然规模是和 n 同量级，
    # 示例：设 s = n（可按需要修改为其他生成方式）
    s = n

    # 预处理 p 数组
    global p
    p = [0]
    for i in range(1, 19):
        p.append(p[-1] + 9 * (10 ** i - 1))

    def find(curr_pos, max_pos, curr_s, choose):
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
            return find(curr_pos - 1, max_pos, curr_s - curr_val, choose)
        return False

    choose = [0] * 19
    ans = n + 1
    for num_digit in range(1, 19):
        for i in range(1, num_digit + 1):
            choose[i] = 0
        if find(num_digit, num_digit, s, choose):
            res = 0
            for i in range(num_digit, -1, -1):
                res = res * 10 + choose[i]
            ans = min(ans, res)
            break
    result = n - ans + 1
    # print(result)
    pass
    return result


# 示例：调用 main，规模 n 可按需要调整
if __name__ == "__main__":
    main(1000000)