def main(n):
    # 生成长度为 n 的二进制字符串 s，确保确定性
    if n <= 0:
        s = ""
    else:
        # 生成按位取模构造的 01 串
        s = "".join('0' if i % 2 == 0 else '1' for i in range(n))

    x = s.count('0')
    if s == '0':
        print('0')
    else:
        print('1' + '0' * x)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的取值做规模实验
    main(10)