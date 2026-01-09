def main(n):
    # 生成长度为 n 的二进制字符串，保证不全为 '0'
    if n <= 0:
        return
    # 构造方式：前半部分为 '1'，后半部分交替 '0' 和 '1'
    half = n // 2
    s = '1' * (half if half > 0 else 1) + ''.join('0' if i % 2 == 0 else '1' for i in range(n - (half if half > 0 else 1)))
    if set(s) == {'0'}:
        s = '1' + s[1:]
    if s == '0':
        # print(0)
        pass

    else:
        # print("1" + "0" * s.count('0'))
        pass
if __name__ == "__main__":
    main(10)