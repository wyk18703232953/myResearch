def main(n):
    # 构造确定性的字符串，长度为 n，字符为循环的 'a'~'z'
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))

    while True:
        if len(s) == 1:
            # print(0)
            pass
            break
        elif s == s[::-1]:
            s = s[1:]

        else:
            # print(len(s))
            pass
            break


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值
    main(10)