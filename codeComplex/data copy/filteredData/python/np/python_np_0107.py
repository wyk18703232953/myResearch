import math

def main(n):
    # 生成确定性的 a 和 b，规模由 n 控制
    # a 和 b 的长度均为 n
    # a 只包含 '+' 和 '-'，b 包含 '+', '-', '?'
    a = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    b_chars = []
    for i in range(n):
        r = i % 3
        if r == 0:
            b_chars.append('+')
        elif r == 1:
            b_chars.append('-')
        else:
            b_chars.append('?')
    b = ''.join(b_chars)

    i = a.count('+')
    j = a.count('-')
    k = b.count('+')
    l = b.count('-')
    m = b.count('?')
    c1 = (i - j)
    c2 = (k - l)
    c = abs(c1 - c2)
    w = m - c
    x = w // 2
    y = w // 2 + c
    if (c == 0 and m == 0):
        result = 1.0
    elif (c > m):
        result = 0.0
    else:
        x_val = math.factorial(m) // (math.factorial(x) * math.factorial(y))
        result = x_val / pow(2, m)
    print(result)
    return result

if __name__ == "__main__":
    main(10)