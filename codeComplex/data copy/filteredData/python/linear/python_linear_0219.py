def main(n):
    # 确定性生成输入字符串 b，长度为 n，包含 '0' 和 '1'
    if n <= 0:
        b = "1"

    else:
        # 生成一个周期性模式，保证含有 0 和 1
        b_list = [('0' if i % 3 == 0 else '1') for i in range(n)]
        b = ''.join(b_list)

    num = len(b)  # 由 b 确定性得到 num

    if b == '0' or b == '1':
        # print(b)
        pass

    else:
        s = len(list(filter(lambda x: x == '0', b)))
        # print('1' + '0' * s)
        pass
if __name__ == "__main__":
    main(10)