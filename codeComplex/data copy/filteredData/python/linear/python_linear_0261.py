def main(n):
    # 生成确定性字符串，长度为 n，使用周期性字符模式
    if n <= 0:
        s = ""

    else:
        chars = "abcd"
        s = "".join(chars[i % len(chars)] for i in range(n))

    c = 0
    c1 = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - i - 1]:
            c += 1
    for i in range(len(s)):
        if s[i] == s[0]:
            c1 += 1
    if c1 == len(s):
        # print(0)
        pass
    elif c == len(s) // 2:
        # print(len(s) - 1)
        pass

    else:
        # print(len(s))
        pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 进行规模实验
    main(10)