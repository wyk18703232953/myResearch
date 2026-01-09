def main(n):
    # 生成一个确定性的测试字符串 s，长度为 n，含有正负数和不同结尾
    if n <= 0:
        s = "0"

    else:
        # 周期性构造字符，保证可复现
        chars = ['-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        s = ''.join(chars[i % len(chars)] for i in range(n))
        # 保证第一个字符有意义：负号开头或数字开头
        if s[0] not in "-0123456789":
            s = '0' + s[1:]
        # 进一步固定首字符：偶数 n 用 '-' 开头，奇数 n 用数字开头
        if n % 2 == 0:
            s = '-' + s[1:]

        else:
            if s[0] == '-':
                s = '1' + s[1:]

    # 以下为原有逻辑，去掉 input()
    n_len = len(s)
    if s[0] == '-':
        if s[n_len - 1] < s[n_len - 2]:
            s = s[::-1]
            s = s.replace(s[1], "", 1)
            s = s[::-1]

        else:
            s = s[::-1]
            s = s.replace(s[0], "", 1)
            s = s[::-1]
        if s == "-0":
            # print("0")
            pass

        else:
            # print(s)
            pass

    else:
        # print(s)
        pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 观察时间复杂度表现
    main(10)