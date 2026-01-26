import math

def main(n):
    # n 表示字符串长度规模，至少为 1
    if n < 1:
        n = 1

    # 构造 s1：前一半 '+', 后一半 '-'
    half = n // 2
    s1 = '+' * half + '-' * (n - half)

    # 构造 s2：将前一半位置设为 '?', 后一半与 s1 相同
    s2 = '?' * half + s1[half:]

    plus = s1.count('+')
    minus = s1.count('-')

    pre_plus = s2.count('+')
    pre_minus = s2.count('-')

    req_plus = plus - pre_plus
    req_minus = minus - pre_minus

    if req_minus < 0 or req_plus < 0:
        print('%.12f' % 0)
    else:
        unknowns = len(s1) - (pre_minus + pre_plus)
        if unknowns == 0:
            print('%.12f' % 1)
        else:
            den = pow(2, unknowns)
            num = math.factorial(unknowns) / (math.factorial(req_plus) * math.factorial(req_minus))
            ans = num / den
            print('%.12f' % ans)

if __name__ == "__main__":
    main(10)