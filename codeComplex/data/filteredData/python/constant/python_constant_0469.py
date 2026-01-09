def x(a, b):
    if a > b:
        return 1

    else:
        return 0

def main(n):
    # 确定性生成输入数据，n 作为规模参数
    # 原代码结构：
    # n (未实际使用)
    # a1 a2
    # b1 b2
    # c1 c2

    # 保证有意义的规模
    if n < 1:
        n = 1

    # 生成 a1, a2, b1, b2, c1, c2
    # 使用简单算术，完全确定
    a1 = n
    a2 = n // 2 + 1
    b1 = n // 3 + 2
    b2 = n // 4 + 3
    c1 = n // 5 + 4
    c2 = n // 6 + 5

    if (a1 - a2) == (b1 - b2):
        # print("NO")
        pass
    elif (a1 + a2) == (b1 + b2):
        # print("NO")
        pass
    elif a1 == b1:
        # print("NO")
        pass
    elif a2 == b2:
        # print("NO")
        pass
    elif (a1 - a2) == (c1 - c2):
        # print("NO")
        pass
    elif (a1 + a2) == (c1 + c2):
        # print("NO")
        pass
    elif a1 == c1:
        # print("NO")
        pass
    elif a2 == c2:
        # print("NO")
        pass

    else:
        if (x(a1, b1) == x(a1, c1)) and (x(a2, b2) == x(a2, c2)):
            # print("YES")
            pass

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    main(10)