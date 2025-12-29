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

def query2(c, d):
    ans = mock_query(c, d)
    # 调试信息可按需保留或删除
    # print('? {:08b} {:08b} --> {}'.format(c, d, ans))
    return ans

def solve(max_bit):
    a = 0
    b = 0
    last_ans = query2(0, 0)

    pos = max_bit
    while pos >= 0:
        bit = 1 << pos

        ans = query2(a + bit, b + bit)
        if (last_ans, ans) == (1, -1):
            a += bit
            last_ans = query2(a, b)
        elif (last_ans, ans) == (-1, 1):
            b += bit
            last_ans = query2(a, b)
        else:
            last_ans = ans
            ans = query2(a + bit, b)
            if ans == -1:
                a += bit
                b += bit

        pos -= 1

    # 返回最终求得的 a, b
    return a, b

def main(n):
    """
    n: 规模参数，这里解释为最大比特位数。
       将在 [0, n-1] 比特位范围内恢复 a, b。
    同时根据 n 生成测试数据：
      a0, b0 的有效位数不超过 n，比特位在 [0, n-1] 内。
    """
    global a0, b0
    if n <= 0:
        return 0, 0

    # 生成规模为 n 的测试数据：a0, b0 的值限制在 [0, 2^n - 1]
    mask = (1 << n) - 1
    # 这里为了确定性，仍旧用给定的 3,1 但截断到 n 比特
    a0 = 3 & mask
    b0 = 1 & mask

    # 在最高比特位为 n-1 的范围内求解
    return solve(n - 1)

if __name__ == "__main__":
    # 示例：n = 30，对应原代码从 bit 29 到 0
    a, b = main(30)
    print('!', a, b)