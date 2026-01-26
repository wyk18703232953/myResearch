import math

def main(n):
    # n 表示字符串长度
    if n <= 0:
        return
    # 构造 s1：前 n//2 个为 '+'，剩余为 '-'
    s1 = ''.join('+' if i < n // 2 else '-' for i in range(n))
    # 构造 s2：按下述周期性规则生成，确保函数完全确定性
    # i % 3 == 0 -> '+', i % 3 == 1 -> '-', i % 3 == 2 -> '?'
    s2 = ''.join('+' if i % 3 == 0 else '-' if i % 3 == 1 else '?' for i in range(n))

    ps1 = 0
    ms1 = 0
    ps2 = 0
    ms2 = 0
    qs2 = 0

    for ch in s1:
        if ch == '+':
            ps1 += 1
        if ch == '-':
            ms1 += 1

    for ch in s2:
        if ch == '+':
            ps2 += 1
        if ch == '-':
            ms2 += 1
        if ch == '?':
            qs2 += 1

    if ps2 <= ps1 and ms2 <= ms1:
        result = math.factorial(qs2) / math.factorial(ps1 - ps2) / math.factorial(ms1 - ms2) * (0.5 ** qs2)
        print(result)
    else:
        print(0.00000000)


if __name__ == "__main__":
    main(10)