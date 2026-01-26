def main(n):
    # 对应原程序的输入：
    # n: 字符串长度
    # s: 由 '0' 和 '1' 组成的长度为 n 的字符串，确定性构造
    if n <= 0:
        return

    # 确定性构造一个长度为 n 的二进制字符串
    # 规则：第 i 位 (0-based) 为 '1' 当且仅当 (i % 3 == 0)，否则为 '0'
    s = ''.join('1' if i % 3 == 0 else '0' for i in range(n))

    if n == 1:
        # print(s)
        pass

    else:
        zeros = s.count('0')
        # print('1' + zeros * '0')
        pass
if __name__ == "__main__":
    # 示例：以 n = 10 运行一次
    main(10)