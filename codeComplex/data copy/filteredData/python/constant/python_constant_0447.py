def main(n):
    # 映射 n 到字符串长度规模
    # 保持原始结构：一串 '4'，最后一个是 '5'；以及全是 '5' 的串
    # 原程序是 300 个 '4' + 1 个 '5'，以及 301 个 '5'
    # 这里令长度 = max(1, n)
    length = max(1, n)

    if length == 1:
        a = '5'  # 只有最后一个字符
        b = '5'

    else:
        a = '4' * (length - 1) + '5'
        b = '5' * length

    # print(a)
    pass
    # print(b)
    pass
if __name__ == "__main__":
    main(300)