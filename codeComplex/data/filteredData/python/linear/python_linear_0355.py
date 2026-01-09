def main(n):
    # 生成长度为 n 的数字字符串 s，完全确定性
    # 例如循环使用 0-9
    digits = [str(i % 10) for i in range(n)]
    s = "".join(digits)

    count = 0
    i = 0
    while i < len(s):
        if int(s[i]) % 3 == 0:
            count += 1
            i += 1
        elif i < len(s) - 1 and (int(s[i:i+2]) % 3 == 0 or int(s[i+1]) % 3 == 0):
            count += 1
            i += 2
        elif i < len(s) - 2 and (int(s[i+1:i+3]) % 3 == 0 or int(s[i:i+3]) % 3 == 0 or s[i+2] == '0'):
            count += 1
            i += 3

        else:
            i += 1

    # print(count)
    pass
if __name__ == "__main__":
    main(10000)