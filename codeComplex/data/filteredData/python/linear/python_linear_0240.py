from collections import Counter

def f(x):
    return max(list(Counter(x).values()))

def v(x, l):
    if x == l:
        return x - 1

    else:
        return x + 1

def main(n):
    # 映射：n 作为字符串长度和 n 作为数值 n
    length = max(1, n)
    z = ''.join(chr(ord('a') + (i % 3)) for i in range(length))
    s_b = ''.join(chr(ord('b') + (i % 3)) for i in range(length))
    s_c = ''.join(chr(ord('c') + (i % 3)) for i in range(length))

    l = len(z)
    a = f(z)
    b = f(s_b)
    c = f(s_c)

    # 将 n 同时作为原程序中的 n
    n_val = n

    if n_val == 1:
        a, b, c = v(a, l), v(b, l), v(c, l)
        if a > b and a > c:
            # print("Kuro")
            pass
        elif b > a and b > c:
            # print("Shiro")
            pass
        elif c > a and c > b:
            # print("Katie")
            pass

        else:
            # print("Draw")
            pass
    elif (l - a <= n_val) + (l - b <= n_val) + (l - c <= n_val) >= 2:
        # print("Draw")
        pass
    elif a > b and a > c:
        # print("Kuro")
        pass
    elif b > a and b > c:
        # print("Shiro")
        pass
    elif c > a and c > b:
        # print("Katie")
        pass

    else:
        # print("Draw")
        pass
if __name__ == "__main__":
    main(10)