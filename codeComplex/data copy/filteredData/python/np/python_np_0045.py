from math import factorial as fc

def per(a, b):
    return fc(a + b) / (fc(a) * fc(b))

def generate_test_strings(n):
    """
    根据规模 n 生成两行字符串 s, s1，用于测试。
    n 控制总长度，约一半给 s，一半给 s1。
    字符只包含 '+', '-', '?'。
    """
    # 保证最小长度
    n = max(n, 2)

    len_s = n // 2
    len_s1 = n - len_s

    # 简单生成：前 1/3 是 '+', 中间 1/3 是 '-', 剩余是 '?'
    def build_string(L):
        a = L // 3
        b = (L - a) // 2
        c = L - a - b
        return "+" * a + "-" * b + "?" * c

    s = build_string(len_s)
    s1 = build_string(len_s1)
    return s, s1

def main(n):
    import sys

    s, s1 = generate_test_strings(n)

    x = s.count("+")
    y = s.count("-")
    x1 = s1.count("+")
    y1 = s1.count("-")
    p = x - y
    p1 = x1 - y1
    q = s1.count("?")
    dif = p - p1

    if q < abs(p1 - p) or dif > q:
        # print(0.0)
        pass
        return

    m = abs(y - y1)
    pl = abs(x - x1)
    # print(per(m, pl) / (2 ** (m + pl)))
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可改为任意正整数规模
    main(10)