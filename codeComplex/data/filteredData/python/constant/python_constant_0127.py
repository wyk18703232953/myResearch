import random

def main(n: int):
    """
    n 用于控制测试数据规模，这里理解为：生成一个在 [-10^n, 10^n] 范围内的随机整数。
    然后对该整数执行与原程序相同的逻辑。
    """
    # 生成测试数据：一个规模由 n 控制的随机整数
    if n <= 0:
        n = 1
    limit = 10 ** n
    value = random.randint(-limit, limit)
    money = str(value)
    initi = money

    if int(money) < 0:
        lst_dig = money[-1]
        lsec_dig = money[-2]
        if int(lst_dig) > int(lsec_dig):
            money = money[:-2] + money[-2]
        else:
            money = money[:-2] + money[-1]
        print(int(money))
    else:
        lst_dig = money[-1]
        lsec_dig = money[-2]
        if int(lst_dig) > int(lsec_dig):
            money = money[:-2] + money[-1]
        else:
            money = money[:-2] + money[-2]
        if int(initi) >= int(money):
            print(initi)
        else:
            print(money)


if __name__ == "__main__":
    # 示例调用：n = 3
    main(3)