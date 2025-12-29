from math import ceil

def main(n: int):
    # 这里简单地把规模 n 作为原程序中的 n 直接使用
    if n == 1:
        print(1)
        return
    if n == 2:
        print('1 2')
        return
    elif n == 3:
        print('1 1 3')
        return

    o = 0
    if n & 1:
        n -= 1
        o = 1

    ans = '1 ' * ceil(n / 2)
    i = 1
    t = n
    n = ceil(n / 2)
    j = 2

    while n > 1:
        ans += (str(j) + ' ') * ((n // 2) if t & 1 else ceil(n / 2))
        i += 1
        j = pow(2, i)
        n //= 2

    print(('1 ' if o else '') + ans + str((j // 2) * (t // (j // 2))))


if __name__ == "__main__":
    # 示例：自动生成一个规模为 30 的测试
    main(30)