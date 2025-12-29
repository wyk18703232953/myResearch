import random

def main(n: int):
    # 1. 生成测试数据：根据规模 n 生成一个字符串 sb
    #   - 字符串长度 nb = n
    #   - 字符范围 '0' ~ '9'
    nb = n
    # 保证首位不为 '0'，否则整数比较会有前导零问题
    first_digit = random.choice('123456789') if nb > 0 else '0'
    other_digits = ''.join(random.choice('0123456789') for _ in range(max(nb - 1, 0)))
    sb = first_digit + other_digits if nb > 0 else "0"

    # 2. 按原逻辑构造 sa（被重排的数字串）
    # 为了构造有意义的测试：让 sa 与 sb 长度相同，且包含同样数量级的数据
    # 这里简单生成与 sb 长度相同的随机数字串，并按原代码排序
    sa_raw = ''.join(random.choice('0123456789') for _ in range(len(sb)))
    sa = sorted(sa_raw, reverse=True)
    na = len(sa)

    # 原始逻辑开始
    if len(sb) > na:
        print(''.join(sa))
        return

    ans = ''
    while sa:
        for i in range(len(sa)):
            # 将第 i 个字符放在当前位置，其余按升序排在后面，形成 new
            new = ans + sa[i] + ''.join(sorted(sa[:i] + sa[i + 1:]))
            if int(new) <= int(sb):
                ans += sa[i]
                sa.pop(i)
                break
    print(ans)


if __name__ == "__main__":
    # 示例：可修改 n 以测试不同规模
    main(5)