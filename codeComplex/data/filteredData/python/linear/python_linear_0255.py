def main(n):
    # 生成确定性字符串作为输入，长度为 n
    # 构造规则：前半部分递增字符，后半部分为其逆序，整体形成回文结构
    base = [chr(ord('a') + (i % 26)) for i in range((n + 1) // 2)]
    if n % 2 == 0:
        s_list = base + base[::-1]

    else:
        s_list = base + base[-2::-1]
    s = "".join(s_list)

    # 原始逻辑
    while s != "":
        if s == s[::-1]:
            s = s[:(len(s) - 1)]

        else:
            break
    # print(len(s))
    pass
if __name__ == "__main__":
    main(10)