from math import factorial

def main(n):
    # 构造两个长度为 n 的只含 '+' 和 '-' 的字符串
    # s1: 前半部分为 '+', 后半部分为 '-'
    # s2: 交替出现 '+' 和 '-'
    s1 = ''.join('+' if i < n // 2 else '-' for i in range(n))
    s2 = ''.join('+' if i % 2 == 0 else '-' for i in range(n))

    a = s1.count('+') - s2.count('+')
    b = s1.count('-') - s2.count('-')

    if a < 0 or b < 0:
        print(0)
        return

    ans = factorial(a + b) / factorial(a) / factorial(b)
    ans /= (2 ** (a + b))
    print("%.10f" % ans)


if __name__ == "__main__":
    main(10)