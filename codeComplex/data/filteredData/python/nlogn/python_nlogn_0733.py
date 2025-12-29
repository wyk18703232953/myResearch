import random

def main(n: int):
    # 根据规模 n 生成 3 张牌，格式如 "1m", "9p", etc.
    # 这里假定花色为 'm','p','s'，数字 1~9
    suits = ['m', 'p', 's']
    cards = []
    for _ in range(3):
        num = random.randint(1, min(9, max(1, n)))
        suit = random.choice(suits)
        cards.append(f"{num}{suit}")

    # 原始逻辑开始
    a = [str(i) for i in cards]
    a.sort()
    first = a[0]
    second = a[1]
    third = a[2]
    firstnum = int(first[0])
    secondnum = int(second[0])
    thirdnum = int(third[0])
    if first == second:
        if second == third:
            print(0)
        else:
            print(1)
    elif second == third:
        print(1)
    elif (first[1] == second[1] and second[1] == third[1]):
        if (firstnum + 1 == secondnum and secondnum + 1 == thirdnum):
            print(0)
        elif (firstnum + 1 == secondnum or firstnum + 2 == secondnum):
            print(1)
        elif (secondnum + 1 == thirdnum or secondnum + 2 == thirdnum):
            print(1)
        else:
            print(2)
    elif (first[1] == second[1] and (firstnum + 1 == secondnum or firstnum + 2 == secondnum)):
        print(1)
    elif (second[1] == third[1] and (secondnum + 1 == thirdnum or secondnum + 2 == thirdnum)):
        print(1)
    elif (first[1] == third[1] and (firstnum + 1 == thirdnum or firstnum + 2 == thirdnum)):
        print(1)
    else:
        print(2)


if __name__ == "__main__":
    # 示例调用
    main(9)