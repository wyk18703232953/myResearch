def main(n):
    # 原程序逻辑：
    # n, s = int(input()), input() * 2
    # h = s.count('H') // 2
    # print(h - max(s[i:i + h].count('H') for i in range(n)))
    #
    # 需要构造一个长度为 n 的字符串 s_original，然后令 s = s_original * 2

    # 确定性构造长度为 n 的字符串，由 'H' 和 '.' 组成
    # 例如：索引为 0,3,6,... 为 'H'，其余为 '.'
    s_original = ''.join('H' if i % 3 == 0 else '.' for i in range(n))
    s = s_original * 2

    h = s.count('H') // 2
    if n == 0 or h == 0:
        # print(0)
        pass
        return

    max_h_in_window = 0
    for i in range(n):
        count_h = s[i:i + h].count('H')
        if count_h > max_h_in_window:
            max_h_in_window = count_h

    # print(h - max_h_in_window)
    pass
if __name__ == "__main__":
    # 示例：可根据需要修改 n 进行规模实验
    main(10)