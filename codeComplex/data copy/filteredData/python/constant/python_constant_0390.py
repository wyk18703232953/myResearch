def main(n):
    # n 表示每一行字符串的长度
    if n < 2:
        # 原算法在 len(line_1) - 1 上循环，长度 < 2 则循环不执行
        # print(0)
        pass
        return

    # 确定性生成两行字符串：
    # line_1: 周期为 3，模式 'O', 'X', 'O'
    # line_2: 周期为 4，模式 'X', 'O', 'O', 'X'
    s1 = ''.join('X' if i % 3 == 1 else 'O' for i in range(n))
    s2 = ''.join('O' if i % 4 in (1, 2) else 'X' for i in range(n))

    line_1 = [c for c in s1]
    line_2 = [c for c in s2]

    no = 0
    for i in range(len(line_1) - 1):
        if line_1[i] != 'X' and line_2[i] != 'X':
            if line_1[i + 1] != 'X':
                no += 1
                line_1[i] = 'X'
                line_2[i] = 'X'
                line_1[i + 1] = 'X'

            elif line_2[i + 1] != 'X':
                no += 1
                line_1[i] = 'X'
                line_2[i] = 'X'
                line_2[i + 1] = 'X'

        elif line_1[i] != 'X' and line_1[i + 1] != 'X' and line_2[i + 1] != 'X':
            no += 1
            line_1[i] = 'X'
            line_1[i + 1] = 'X'
            line_2[i + 1] = 'X'

        elif line_2[i] != 'X' and line_1[i + 1] != 'X' and line_2[i + 1] != 'X':
            no += 1
            line_2[i] = 'X'
            line_1[i + 1] = 'X'
            line_2[i + 1] = 'X'

    # print(no)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的大小进行时间复杂度实验
    main(10)