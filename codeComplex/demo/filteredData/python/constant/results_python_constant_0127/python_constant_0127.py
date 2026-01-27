def main(n):
    # n 控制要生成多少个测试用例，各种长度的整数串
    # 生成确定性的字符串形式的整数 money_list
    money_list = []

    # 1. 简单正数
    for i in range(1, n + 1):
        money_list.append(str(i * 123))

    # 2. 简单负数
    for i in range(1, n + 1):
        money_list.append(str(-i * 123))

    # 3. 包含不同位数、尾数变化等
    for i in range(1, n + 1):
        val = i * 100 + (i % 10) * 10 + (i // 10) % 10
        money_list.append(str(val))
        money_list.append(str(-val))

    results = []

    for money in money_list:
        initi = money
        if int(money) < 0:
            lst_dig = money[-1]
            lsec_dig = money[-2]
            if int(lst_dig) > int(lsec_dig):
                money = money[:-2] + money[-2]

            else:
                money = money[:-2] + money[-1]
            results.append(int(money))

        else:
            lst_dig = money[-1]
            lsec_dig = money[-2]
            if int(lst_dig) > int(lsec_dig):
                money = money[:-2] + money[-1]

            else:
                money = money[:-2] + money[-2]
            if int(initi) >= int(money):
                results.append(int(initi))

            else:
                results.append(int(money))

    # 为了有输出行为，打印所有结果的和（确定性单一输出）
    total = 0
    for x in results:
        total += x
    # print(total)
    pass
if __name__ == "__main__":
    main(1000)