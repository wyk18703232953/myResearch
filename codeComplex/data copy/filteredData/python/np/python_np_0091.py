from math import factorial


def nCr(n, r):
    f = factorial
    return f(n) / f(r) / f(n - r)


def main(n):
    # 生成确定性的输入：
    # s1 为长度 n 的字符串，由前 n//2 个 '+' 和后 n - n//2 个 '-' 组成
    # s2 为长度 n 的字符串，其中位置 i:
    #   若 i % 3 == 0: '+'
    #   若 i % 3 == 1: '-'
    #   否则: '?'
    s1 = ''.join('+' if i < n // 2 else '-' for i in range(n))
    s2 = ''.join('+' if i % 3 == 0 else '-' if i % 3 == 1 else '?' for i in range(n))

    s1_pos = s1.count('+')
    s2_pos = s2.count('+')
    s1_neg = s1.count('-')
    s2_neg = s2.count('-')
    s1_q = s2.count('?')

    ans = 0
    if s1_q == 0:
        if s1_pos == s2_pos:
            ans = 1
        else:
            ans = 0
    else:
        diff1 = s1_pos - s2_pos
        if diff1 > s1_q or diff1 < 0:
            ans = 0
        else:
            ans = nCr(s1_q, diff1) / 2 ** s1_q

    print('{:.12f}'.format(ans))


if __name__ == "__main__":
    main(10)