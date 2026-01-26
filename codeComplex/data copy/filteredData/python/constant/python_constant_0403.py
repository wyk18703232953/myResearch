def ch_x(stri, n):
    res = ''
    for i in range(len(stri)):
        if i != n:
            res += stri[i]

        else:
            res += 'x'
    return res


def core(a, b):
    n = 0
    a = list(a)
    b = list(b)
    for i in range(0, len(a)):
        if a[i] == '0' and b[i] == '0':
            c = [i - 1, i + 1]
            for e in c:
                if 0 <= e < len(a):
                    if a[e] == '0':
                        n += 1
                        a = ch_x(a, e)
                        break
                    if b[e] == '0':
                        n += 1
                        b = ch_x(b, e)
                        break
            a = ch_x(a, i)
            b = ch_x(b, i)
    return n


def main(n):
    length = max(1, n)
    # 生成两个长度为 length 的仅包含 '0' 和 '1' 的字符串
    # 规则：a[i] = '0' if i % 2 == 0 else '1'
    #       b[i] = '0' if i % 3 == 0 else '1'
    a = ''.join('0' if i % 2 == 0 else '1' for i in range(length))
    b = ''.join('0' if i % 3 == 0 else '1' for i in range(length))
    result = core(a, b)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)