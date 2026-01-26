import math

def main(n):
    # 生成长度为 n 的目标串 a，由 '+' 和 '-' 构成，确定性规则：奇偶位交替
    a = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    # 生成长度为 n 的待填串 b，其中部分为 '?'，其余与 a 相反，用于产生不确定格
    # 规则：下标 % 3 == 0 为 '?', 其余为与 a[i] 相反的符号
    b_chars = []
    for i in range(n):
        if i % 3 == 0:
            b_chars.append('?')
        else:
            b_chars.append('-' if a[i] == '+' else '+')
    b = ''.join(b_chars)

    c = 0
    d = 0
    q = 0

    for ch in a:
        if ch == "+":
            c += 1
        elif ch == "-":
            c -= 1

    for ch in b:
        if ch == "+":
            d += 1
        elif ch == "-":
            d -= 1
        else:
            q += 1

    if c == d:
        print((math.factorial(q)/(math.factorial(q/2)*math.factorial(q/2)))/(2**q))
    else:
        mx = d + q
        mn = d - q
        if c > mx or c < mn:
            print(0.0)
        else:
            ans = c - d
            if ans > 0:
                print((math.factorial(q)/(math.factorial(((q-ans)/2)+ans)*math.factorial((q-ans)/2)))/(2**q))
            else:
                print((math.factorial(q)/(math.factorial((q-ans)/2)*math.factorial(((q-ans)/2)+ans)))/(2**q))


if __name__ == "__main__":
    main(10)