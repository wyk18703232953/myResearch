def main(n):
    # 原程序逻辑：
    # n, s = int(input()), input() * 2
    # h = s.count('H') // 2
    # print(h - max(s[i:i + h].count('H') for i in range(n)))

    # 确定性生成长度为 n 的字符串 s_base，由 'H' 和 'T' 组成
    # 规则：i % 3 == 0 -> 'H'，否则 'T'
    s_base = ''.join('H' if i % 3 == 0 else 'T' for i in range(n))

    s = s_base * 2
    h = s.count('H') // 2
    # 为防止极小 n 导致 h 为 0 的无意义情况，这里仍按原逻辑执行
    result = h - max(s[i:i + h].count('H') for i in range(n)) if n > 0 else 0
    # print(result)
    pass
if __name__ == "__main__":
    main(10)