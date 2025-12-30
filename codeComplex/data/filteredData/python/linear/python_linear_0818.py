import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 让 turns = n，candies 为一个在 1 到 n*(n+1)//2 范围内的随机整数
    turns = n
    max_candies = turns * (turns + 1) // 2
    candies = random.randint(1, max_candies)

    summ = 0
    turn = 0
    while candies != summ - (turns - turn):
        turn += 1
        summ += turn
    print(turns - turn)

if __name__ == "__main__":
    # 示例运行：可修改 n 测试不同规模
    main(10)