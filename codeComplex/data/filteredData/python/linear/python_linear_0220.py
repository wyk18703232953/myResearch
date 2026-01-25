def main(n):
    # 生成长度为 n 的只含 '0' 和 '1' 的字符串 a，且包含至少一个 '1'
    # 规则：第一个字符为 '1'，后续根据 (i % 3) 决定是 '0' 还是 '1'
    if n <= 0:
        a = ""
    else:
        chars = []
        for i in range(n):
            if i == 0:
                chars.append("1")
            else:
                if i % 3 == 0:
                    chars.append("1")
                else:
                    chars.append("0")
        a = "".join(chars)

    zero = 0
    for i in range(len(a)):
        if a[i] == "0":
            zero += 1
    if "1" in a:
        print("1", end="")
        print("0" * zero)
    else:
        print("0" * zero)


if __name__ == "__main__":
    main(10)