from math import gcd

def main(n):
    d = dict()
    qs = []
    for i in range(n):
        # 确定性构造原程序中的字符串形式 "(a+b)/c"
        a = i + 1
        b = (i * 2 + 3) % (n + 5) + 1
        c = (i * 3 + 7) % (n + 7) + 1
        s = "(" + str(a) + "+" + str(b) + ")/" + str(c)

        # 原始解析逻辑
        a_parsed = int(s[1:s.index('+')])
        b_parsed = int(s[s.index('+') + 1: s.index(')')])
        c_parsed = int(s[s.index(')') + 2:])

        a_sum = a_parsed + b_parsed
        gc = gcd(a_sum, c_parsed)
        res = (a_sum // gc, c_parsed // gc)
        qs.append(res)
        if res in d:
            d[res] += 1

        else:
            d[res] = 1

    for q in qs:
        # print(d[q], end=' ')
        pass
if __name__ == "__main__":
    main(10)