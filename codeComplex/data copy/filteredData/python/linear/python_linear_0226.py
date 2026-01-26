def main(n):
    # n 表示二进制字符串长度
    if n <= 0:
        return

    # 构造一个确定性的二进制字符串：'10' 循环填充到长度 n
    pattern = ['1', '0']
    binary_number = ''.join(pattern[i % 2] for i in range(n))

    if binary_number == '0':
        # print('0')
        pass

    else:
        count_0 = sum(1 for b in binary_number if b == '0')
        count_1 = sum(1 for b in binary_number if b == '1')
        # print('1' + '0' * count_0)
        pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模
    main(10)