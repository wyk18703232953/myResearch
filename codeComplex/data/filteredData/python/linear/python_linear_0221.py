def main(n):
    # 生成长度为 n 的二进制字符串 s，包含 '0' 和 '1'
    # 确定性规则：第 i 位为 '0' 如果 i % 3 == 0，否则为 '1'
    s = ''.join('0' if i % 3 == 0 else '1' for i in range(n))

    x = s.count('0')
    if s == '0':
        result = '0'

    else:
        result = '1' + '0' * x
    # print(result)
    pass
if __name__ == "__main__":
    main(10)