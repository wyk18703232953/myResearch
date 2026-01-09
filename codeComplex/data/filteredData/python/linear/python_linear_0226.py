def main(n):
    # n 作为二进制字符串长度
    if n <= 0:
        binary_number = "0"

    else:
        # 构造一个确定性的长度为 n 的二进制字符串
        # 例如：按 i % 2 交替生成 '0' 和 '1'
        binary_number = ''.join('0' if i % 2 == 0 else '1' for i in range(n))

    if binary_number == '0':
        # print('0')
        pass

    else:
        count_0 = sum(1 for b in binary_number if b == '0')
        count_1 = sum(1 for b in binary_number if b == '1')
        # print('1' + '0' * count_0)
        pass
if __name__ == "__main__":
    main(10)