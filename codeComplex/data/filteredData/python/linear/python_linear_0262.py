def main(n):
    # 生成一个确定性的字符串作为输入，长度为 n
    # 这里使用周期性模式，保证既有可能是回文也可能不是
    if n <= 0:
        s = ""
    else:
        base = "abc"
        s = "".join(base[i % len(base)] for i in range(n))

    # 原程序逻辑
    while len(s) > 0:
        if s != s[::-1]:
            break
        else:
            s = s[1:]
    print(len(s))


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值
    main(10)