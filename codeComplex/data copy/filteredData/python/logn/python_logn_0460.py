a0 = 3
b0 = 1

def mock_query(c, d):
    res = (a0 ^ c) - (b0 ^ d)
    if res > 0:
        return 1
    elif res < 0:
        return -1

    else:
        return 0

def query(c, d):
    # 替代原来的交互：直接调用 mock_query
    return mock_query(c, d)

def solve(max_bit):
    a = 0
    b = 0
    last_ans = query(0, 0)

    pos = max_bit
    while pos >= 0:
        bit = 1 << pos

        ans = query(a + bit, b + bit)
        if (last_ans, ans) == (1, -1):
            a += bit
            last_ans = query(a, b)
        elif (last_ans, ans) == (-1, 1):
            b += bit
            last_ans = query(a, b)

        else:
            last_ans = ans
            ans = query(a + bit, b)
            if ans == -1:
                a += bit
                b += bit

        pos -= 1

    return a, b

def main(n):
    """
    n 作为规模参数使用：
    - 用 n 的二进制位长度作为要处理的比特数。
    - 同时可以根据需要用 n 派生 a0, b0（这里保持固定，也可改为依 n 生成）。
    """
    # 这里简单使用 n 的位长度作为最高位下标
    if n <= 0:
        max_bit = 0

    else:
        max_bit = n.bit_length() - 1

    # 如果希望 a0,b0 随 n 变化，可在此重置为依赖 n 的值
    # 例如：
    # global a0, b0
    # a0 = (1 << (max_bit + 1)) - 1
    # b0 = n

    a, b = solve(max_bit)
    # 主函数中返回结果，而不是打印
    return a, b

if __name__ == "__main__":
    # 示例：以 n=1<<30 规模测试
    res_a, res_b = main(1 << 30)
    # print("!", res_a, res_b)
    pass