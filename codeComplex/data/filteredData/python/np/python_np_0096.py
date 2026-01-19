import math

def main(n):
    # 生成确定性的 s1 和 s2，长度随 n 增长
    # s1 只包含 '+' 和 '-'，s2 还可能包含 '?'
    length = max(1, n)
    s1 = ''.join('+' if i % 2 == 0 else '-' for i in range(length))
    # 对于 s2，每第三个字符设为 '?'，其余依序从 '+', '-' 取
    pattern = ['+', '-']
    s2_chars = []
    for i in range(length):
        if i % 3 == 2:
            s2_chars.append('?')
        else:
            s2_chars.append(pattern[i % 2])
    s2 = ''.join(s2_chars)

    if s2.count('?') == 0:
        if s1.count('+') == s2.count('+') and s1.count('-') == s2.count('-'):
            p = 1
        else:
            p = 0
    else:
        if (s1.count('+') < s2.count('+') != 0) or (s1.count('-') == 0 < s2.count('-') != 0):
            p = 0
        else:
            pl = s1.count('+') - s2.count('+')
            mi = s1.count('-') - s2.count('-')
            p = (math.factorial(pl + mi) / math.factorial(pl) / math.factorial(mi)) / 2 ** (pl + mi)
    print('%1.9f' % p)


if __name__ == "__main__":
    main(10)