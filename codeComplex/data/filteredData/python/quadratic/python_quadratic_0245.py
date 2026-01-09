def get_sign_1(fo):
    def res(s, f=fo):
        if f ** 2 + s ** 2 == 2 * f * s + 1:
            return '1'

        else:
            return '0'
    return res


def get_signs_2(cf, rev):
    cf -= 1
    if rev:
        def res(fo, cff=cf):
            if fo >= cff:
                def res2(s, f=fo):
                    if s == f:
                        return '0'
                    elif s >= cff:
                        return '0'

                    else:
                        return '1'

            else:
                def res2(s, f=fo):
                    if s == f:
                        return '0'

                    else:
                        return '1'
            return res2

    else:
        def res(fo, cff=cf):
            if fo >= cff:
                def res2(s, f=fo):
                    if s == f:
                        return '0'
                    elif s >= cff:
                        return '1'

                    else:
                        return '0'

            else:
                def res2(s):
                    return '0'
            return res2
    return res


def main(n):
    # 生成一组满足原逻辑条件的 (a, b)
    # 需满足：a*b = c，a + b = c + 1
    # 设 b = c，则 a = (c + 1) - c = 1 => a = 1, b = c
    # 即选择 a = 1, b = n-1（当 n > 1 时）
    if n == 1:
        a, b = 1, 1
    elif n == 2:
        # 对于 n = 2 原条件 a+b=c+1 和整型 c 不好同时满足，给一组简单数据
        a, b = 1, 1

    else:
        a, b = 1, n - 1

    c = a * b
    if a + b == c + 1 and (c > 1 or n == 1 or n > 3):
        # print("YES")
        pass

        if c == 1:
            get_sign_f = get_sign_1

        else:
            get_sign_f = get_signs_2(c, c == b)
        for foo in range(n):
            # print(''.join(map(get_sign_f(foo), range(n))))
            pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)