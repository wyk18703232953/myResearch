def main(n):
    # 解释输入结构：
    # 原程序有两个整数输入：turns, candies
    # 将 n 映射为：
    #   turns = n
    #   candies = n * (n + 1) // 2
    # 这样规模含义与 n 成正比，且完全确定。
    turns = n
    candies = n * (n + 1) // 2

    summ = 0
    turn = 0
    while candies != summ - (turns - turn):
        turn += 1
        summ += turn
    result = turns - turn
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)