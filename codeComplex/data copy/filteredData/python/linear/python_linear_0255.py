def main(n):
    # 生成一个确定性的字符串，长度为 n
    # 构造方式：前半部分为升序字母，后半部分为降序字母，保证有一定的非回文结构
    if n <= 0:
        s = ""

    else:
        base = [chr(ord('a') + (i % 26)) for i in range(n)]
        # 为了增加变化，后半部分逆序
        mid = n // 2
        s = "".join(base[:mid] + base[mid:][::-1])

    while s != "":
        if s == s[::-1]:
            s = s[:(len(s) - 1)]

        else:
            break
    # print(len(s))
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 进行调用，可根据需要修改 n
    main(10)