def main(n):
    # 生成一个长度为 n 的数字字符串，使用确定性规则
    # 这里用 (i % 10) 将下标映射到 0-9 的数字字符
    digits = ''.join(str(i % 10) for i in range(n))

    ct = 0
    i = 0
    s = []
    while i < len(digits):
        if not int(digits[i]) % 3:
            ct += 1
            s.clear()

        else:
            t = int(digits[i]) % 3
            if 3 - t in s:
                ct += 1
                s.clear()

            else:
                s.append(t)
        if len(s) == 3:
            ct += 1
            s.clear()
        i += 1

    # print(ct)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)