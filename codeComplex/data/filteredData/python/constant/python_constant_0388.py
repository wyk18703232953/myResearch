from math import inf

def main(n):
    # 生成两个长度为 n 的只含 '0' 和 '1' 的字符串
    # a[0]: 周期 2 模式 '0','1','0','1',...
    # a[1]: 周期 3 模式 '0','0','1','0','0','1',...
    s0 = [('0' if i % 2 == 0 else '1') for i in range(n)]
    s1 = [('0' if i % 3 < 2 else '1') for i in range(n)]

    a = [s0, s1]

    an = [-inf, -inf, -inf]
    if a[0][0] == a[1][0] == '0':
        an[0] = 0
    elif a[0][0] != a[1][0]:
        an[1] = 0
    x = 0
    for i in range(1, len(a[0])):
        if an[0] == 0:
            if a[0][i] == a[1][i] == '0':
                x += 1
                an = [-inf, 0, -inf]
            elif a[0][i] != a[1][i]:
                x += 1
                an = [-inf, -inf, -inf]

            else:
                an = [-inf, -inf, -inf]
        elif an[1] == 0:
            if a[0][i] == a[1][i] == '0':
                x += 1
                an = [-inf, -inf, -inf]
            elif a[0][i] != a[1][i]:
                pass

            else:
                an = [-inf, -inf, -inf]

        else:
            if a[0][i] == a[1][i] == '0':
                an = [0, -inf, -inf]
            elif a[0][i] != a[1][i]:
                an = [-inf, 0, -inf]

            else:
                an = [-inf, -inf, -inf]

    # print(x)
    pass
if __name__ == "__main__":
    main(10)