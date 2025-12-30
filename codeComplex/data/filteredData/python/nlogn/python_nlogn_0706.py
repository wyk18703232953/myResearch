import random

def main(n):
    # 生成测试数据：n 个非负整数
    # 可以根据需要调整数据范围
    game = [random.randint(0, 10**9) for _ in range(n)]

    # 原逻辑开始
    game.append(-1)
    game.sort()
    bitSum = game[1] % 2
    rep = False
    for i in range(1, n):
        bitSum += game[i + 1] % 2
        if game[i] == game[i + 1]:
            if rep:
                print('cslnb')
                return
            else:
                if game[i - 1] == game[i] - 1:
                    print('cslnb')
                    return
                rep = True
    Goal = ((n * (n - 1)) / 2) % 2
    if (bitSum + Goal) % 2 == 0:
        print('cslnb')
    else:
        print('sjfnb')


# 示例调用
if __name__ == "__main__":
    main(5)