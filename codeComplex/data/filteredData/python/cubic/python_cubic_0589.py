import random

def rec(res, digit, rem, b):
    if digit == len(b):
        return res
    # 尝试匹配与 b[digit] 相同的数字
    cur_digit = int(b[digit])
    if rem[cur_digit]:
        r = rem[:]
        r[cur_digit] -= 1
        x = rec(res + b[digit], digit + 1, r, b)
        if x:
            return x
    # 尝试放一个比 b[digit] 小的数字
    for d in range(cur_digit - 1, -1, -1):
        if rem[d]:
            res += str(d)
            rem[d] -= 1
            suf = []
            for i in range(10):
                suf += [str(i)] * rem[i]
            return res + ''.join(sorted(suf, reverse=True))
    return ''


def main(n):
    """
    n 为规模参数：
    - 生成一个长度为 n 的数字串 a
    - 生成一个长度为 n 或 n-1 的数字串 b（随机选择）
    - 然后执行与原程序等价的逻辑并打印结果
    """
    if n <= 0:
        return

    # 生成测试数据 a 和 b
    a_len = n
    # b 的长度为 n 或 n-1，且至少为 1
    b_len = n if n == 1 else random.choice([n, n - 1])

    # 生成不以 0 开头的随机数字串
    def gen_num_str(length):
        if length == 1:
            return str(random.randint(0, 9))
        first = str(random.randint(1, 9))
        rest = ''.join(str(random.randint(0, 9)) for _ in range(length - 1))
        return first + rest

    a = gen_num_str(a_len)
    b = gen_num_str(b_len)

    # 与原逻辑保持一致
    if len(a) < len(b):
        print(''.join(sorted(a, reverse=True)))
        return

    cnt = [0] * 10
    for x in a:
        cnt[int(x)] += 1

    ans = rec('', 0, cnt[:], b)
    print(ans)


if __name__ == "__main__":
    # 示例：使用 n=5 进行测试
    main(5)