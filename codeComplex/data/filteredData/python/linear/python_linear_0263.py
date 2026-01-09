def main(n):
    # 生成确定性字符串，长度为 n
    # 例如：重复 'abc' 模式，长度恰好为 n
    base = "abc"
    s = (base * (n // len(base) + 1))[:n]

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
    main(10)