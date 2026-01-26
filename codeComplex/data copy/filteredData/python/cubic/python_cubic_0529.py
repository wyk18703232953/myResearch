def main(n):
    # 映射：n -> 字符串长度和上界 b 的位数
    length = max(1, n)
    # 生成确定性的字符串 a：循环使用数字 1-9
    a = [str((i % 9) + 1) for i in range(length)]
    # 生成确定性的上界 b：重复 '9' length 次
    b = int('9' * length)

    a, b = sorted(a), int(b)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            c = int(''.join(a))
            a[i], a[j] = a[j], a[i]
            d = int(''.join(a))
            if c <= d <= b:
                continue

            else:
                a[i], a[j] = a[j], a[i]
    # print(''.join(a))
    pass
if __name__ == "__main__":
    main(5)