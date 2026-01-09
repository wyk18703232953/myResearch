def main(n):
    # 规模含义：构造长度为 n 的二进制字符串 a
    # 规则：前半部分为 '1'，后半部分为 '0'
    a = ''.join('1' if i < n // 2 else '0' for i in range(n))

    zero = 0
    for i in range(len(a)):
        if a[i] == "0":
            zero += 1
    if "1" in a:
        # print("1", end="")
        pass
        # print("0" * zero)
        pass

    else:
        # print("0" * zero)
        pass
if __name__ == "__main__":
    main(10)