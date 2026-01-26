import math

def main(n):
    # n 作为字符串长度，至少为 1
    length = max(1, n)

    # 构造第一个字符串 a：周期性使用 '+', '-'，其余用 '+'
    chars_a = ['+', '-']
    a = ''.join(chars_a[i % 2] for i in range(length))

    # 构造第二个字符串 b：同样长度，前半用 '?', 后半模仿 a
    half = length // 2
    b_prefix = '?' * half
    b_suffix = a[half:]
    b = b_prefix + b_suffix

    sa = a.count("+")
    ta = a.count("-")
    sb = b.count("+")
    tb = b.count("-")
    x = b.count("?")
    s = abs(sa - sb)
    t = abs(ta - tb)
    su = math.factorial(s + t)
    re = math.factorial(s)
    sa = math.factorial(t)
    result = su / (re * sa)
    if s + t <= x:
        print(float(result) / float((2 ** x)))
    else:
        print(0)


if __name__ == "__main__":
    main(10)