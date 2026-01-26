def main(n):
    # 生成确定性的测试数据：长度为 n 的只包含 '0','1','2' 的字符串
    # 这里采用简单的算术构造模式，保证可重复性
    chars = ['0', '1', '2']
    s = ''.join(chars[i % 3] for i in range(n))

    one = s.count('1')
    zero = 0
    ind = -1
    for i in range(len(s)):
        if s[i] == '2':
            ind = i
            break
        if s[i] == '0':
            zero += 1
    d = ""
    if ind == -1:
        # print("0" * zero + "1" * one)
        pass
        return
    d = d + "0" * zero + "1" * one
    for i in s[ind:]:
        if i != '1':
            d += i
    # print(d)
    pass
if __name__ == "__main__":
    main(10)