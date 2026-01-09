def main(n):
    # 生成确定性字符串：前 n 个小写字母循环
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = "".join(alphabet[i % 26] for i in range(n))

    while len(s) > 0:
        if s != s[::-1]:
            break

        else:
            s = s[1:]
    # print(len(s))
    pass
if __name__ == "__main__":
    main(10)