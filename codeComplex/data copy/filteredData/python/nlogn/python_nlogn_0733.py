def main(n):
    # 生成确定性输入：n 决定生成的 3 个字符串的数字部分
    # 数字部分在 1~9 循环，花色在 ['m', 'p', 's'] 中循环
    suits = ['m', 'p', 's']
    a = []
    for i in range(3):
        num = (n + i) % 9 + 1  # 1..9
        suit = suits[(n + i) % len(suits)]
        a.append(str(num) + suit)

    a.sort()
    first = a[0]
    second = a[1]
    third = a[2]
    firstnum = int(first[0])
    secondnum = int(second[0])
    thirdnum = int(third[0])
    if first == second:
        if second == third:
            # print(0)
            pass

        else:
            # print(1)
            pass
    elif second == third:
        # print(1)
        pass
    elif first[1] == second[1] and second[1] == third[1]:
        if firstnum + 1 == secondnum and secondnum + 1 == thirdnum:
            # print(0)
            pass
        elif firstnum + 1 == secondnum or firstnum + 2 == secondnum:
            # print(1)
            pass
        elif secondnum + 1 == thirdnum or secondnum + 2 == thirdnum:
            # print(1)
            pass

        else:
            # print(2)
            pass
    elif first[1] == second[1] and (firstnum + 1 == secondnum or firstnum + 2 == secondnum):
        # print(1)
        pass
    elif second[1] == third[1] and (secondnum + 1 == thirdnum or secondnum + 2 == thirdnum):
        # print(1)
        pass
    elif first[1] == third[1] and (firstnum + 1 == thirdnum or firstnum + 2 == thirdnum):
        # print(1)
        pass

    else:
        # print(2)
        pass
if __name__ == "__main__":
    main(10)