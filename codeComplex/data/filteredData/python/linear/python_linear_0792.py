import random

def main(n):
    # 生成规模为 n 的测试数据：n 张麻将牌，格式如 "1m", "9p", "3s"
    # 合法牌集合
    suits = ['m', 'p', 's']
    ranks = [str(i) for i in range(1, 10)]
    all_cards = [r + s for s in suits for r in ranks]

    # 随机生成 n 张牌（允许重复）
    cards = [random.choice(all_cards) for _ in range(n)]

    # 下方是原逻辑的封装与修正
    lm = [0] * 9
    lp = [0] * 9
    ls = [0] * 9

    for item in cards:
        if item[1] == 'm':
            lm[int(item[0]) - 1] += 1
        elif item[1] == 'p':
            lp[int(item[0]) - 1] += 1
        else:
            ls[int(item[0]) - 1] += 1

    # 检查是否有三张相同的牌
    if max(lm) == 3 or max(lp) == 3 or max(ls) == 3:
        result = 0
    else:
        def seq_checker(li):
            flag = 0
            for i in range(9):
                if flag == 0:
                    if li[i] == 1:
                        flag = 1
                else:
                    if li[i] == 1:
                        flag += 1
                    else:
                        break
            return flag

        if seq_checker(lm) == 3 or seq_checker(lp) == 3 or seq_checker(ls) == 3:
            result = 0
        elif max(lm) == 2 or max(lp) == 2 or max(ls) == 2:
            result = 1
        else:
            m = 0
            for i in range(0, 7):
                m = max(
                    sum(lm[i:i + 3]),
                    sum(lp[i:i + 3]),
                    sum(ls[i:i + 3]),
                    m
                )
            result = 3 - m

    # 输出测试数据与结果，便于验证
    print("cards:", cards)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(3) 生成 3 张牌进行测试
    main(3)