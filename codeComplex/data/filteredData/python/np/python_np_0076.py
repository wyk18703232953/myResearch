from math import factorial

def main(n):
    # 根据 n 生成确定性的输入字符串 a, b
    # a: 长度为 n，由 '+', '-' 组成
    # b: 长度为 n，由 '+', '-', '?' 组成
    if n <= 0:
        a = ""
        b = ""
    else:
        # a 中只有 '+' 和 '-'，用 i % 2 决定符号
        a_chars = ['+' if i % 2 == 0 else '-' for i in range(n)]
        a = ''.join(a_chars)
        # b 中包含 '+', '-', '?'，用 i % 3 决定字符
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

    s = 0
    s1 = 0
    c = 0

    for i in a:
        if i == '+':
            s += 1
        else:
            s -= 1

    for i in b:
        if i == '+':
            s1 += 1
        elif i == '-':
            s1 -= 1
        else:
            c += 1

    if c == 0:
        if s == s1:
            print(c + 1)
        else:
            print(c)
    else:
        l = []
        k = c
        i = c
        j = 0
        while i >= 0:
            l.append(k)
            i -= 1
            j += 1
            k = 0
            k += i
            k -= j
        if s1 != 0:
            for i in range(len(l)):
                l[i] += s1
        try:
            c1 = l.index(s)
            k = factorial(c) / (factorial(c - c1) * factorial(c1))
            print(k / pow(2, c))
        except ValueError:
            print(0.0)


if __name__ == "__main__":
    # 示例：可自行修改 n 观察时间随规模变化
    main(10)