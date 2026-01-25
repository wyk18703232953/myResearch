def main(n):
    a = n
    # 生成一个长度至少为 a 的字符串，周期性包含和不包含 "xxx"
    base = "abcxxx"
    if a <= 0:
        b = ""
    else:
        # 构造长度为 a 的字符串
        times = a // len(base) + 1
        b = (base * times)[:a]
    s = 0
    for i in range(a - 2):
        if b[i:i + 3] == 'xxx':
            s = s + 1
    print(s)


if __name__ == "__main__":
    main(10)