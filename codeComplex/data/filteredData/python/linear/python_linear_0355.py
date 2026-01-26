def main(n):
    # 确定性构造长度为 n 的数字串，避免前导 0 全串为 0
    if n <= 0:
        # print(0)
        pass
        return
    s = ''.join(str((i * 7 + 3) % 10) for i in range(n))
    if s[0] == '0':
        s = '1' + s[1:]

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
    main(10)